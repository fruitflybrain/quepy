# coding: utf-8

from quepy.tagger import Word
from quepy.encodingpolicy import assert_valid_encoding
import re
import logging
log = logging.getLogger( 'quepy.spacytagger' )

from neuroarch_nlp.data import neuropils, subregions, colors_values
import spacy
from spacy.attrs import LOWER
from spacy.matcher import Matcher
nlp = spacy.load('en')
matcher = Matcher(nlp.vocab)

# Go through the accepted (English) string representations of neuropil names
# and add the multi-word names to spaCy's rule-based Matcher, so we can merge
# each name as a single token (later), which will slightly simplify the grammar
for db_rep, string_reps in neuropils:
    for string in string_reps:
        lexes = string.split()
        if len( lexes ) > 1:
            # NOTE: The first parameter, the ID, could be specified as the "canonical" neuropil name
            matcher.add( 'NEUROPIL', None, 
                         [ {LOWER: lex.lower()} for lex in lexes ])
#                         label='NEUROPIL' )
# Also merge multi-word subregion names and accepted (English; HTML) color names
for phrase in subregions.keys() + colors_values.keys():
    phrase = phrase.split()
    if len( phrase ) > 1:
        matcher.add( 'SUBREGION', None,
                     [ {LOWER: lex.lower()} for lex in phrase ])
#                     label='SUBREGION' )

compilers = [
    ('presynaptic', re.compile(
     "pre-synaptic|pre- synaptic|pre -synaptic|pre synaptic|pre - synaptic", re.IGNORECASE )),
    ('postsynaptic', re.compile(
     "post-synaptic|post- synaptic|post -synaptic|post synaptic|post - synaptic", re.IGNORECASE ))
]

def collapse( string ):
    for substr, compiler in compilers:
        string = compiler.sub( substr, string )
    return string

def run_spacytagger( string ):
    """
    Runs spacy on `string` and returns a list of
    :class:`quepy.tagger.Word` objects.
    """
    assert_valid_encoding(string)

    # For now, at least, perform our own pre-processing
    # --to ensure terms like "presynaptic" are easily found later.
    string = ' '.join( string.split() )
    string = collapse( string )

    doc = nlp( string )  # NOTE: spaCy expects and returns unicode

    spans = [ (ent_id, label_id, doc[start:end])
             for ent_id, label_id, start, end in matcher( doc ) ]
    for ent_id, label_id, span in spans:
        span.merge( label=label_id, tag='NNP' if label_id else span.root.tag_ )

    # tag_ is the "fine-grained" POS
    words = [ Word(x.text, x.lemma_, x.tag_) for x in doc ]


    # The following is only for logging purposes; if necessary, it could be removed for production
    log.info( ' '.join([ t.text +'['+ str(t.i) +']' for t in doc ]) )
    indent = "  "
    longest = max( len(t.text) for t in doc )
    column = (len(doc) - 1) * len(indent) + longest + 2
    wout = '{:'+ str(column) +'}| '
    def trav_tree( indents, node ):
        log.info( wout.format((indent * indents) + node.text) + ', '.join(
            [ str(x) for x in [
                node.i, node.is_oov, node.lemma_, node.tag_, \
                "<-"+ str(node.left_edge), str(node.right_edge) +"->"] ]) )
        for el in node.children:
            # NOTE: Could also change display based on node.lefts and node.rights
            trav_tree( indents + 1, el ) 
    for sent in doc.sents:
        trav_tree( 0, sent.root )
    log.info( 'Ents:  '+ str(doc.ents) )
    log.info( 'NPs:   '+ str(list(doc.noun_chunks)) )


    return words
