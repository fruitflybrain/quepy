# coding: utf-8

import spacy
from spacy.attrs import LOWER
nlp = spacy.load('en')
nlp.entity.add_label('NEUROPIL')

# Modifier spaCy's Matcher to look for neuropils (as part of its NER).
nlp.matcher.add( 'AL', 'NEUROPIL', {}, [
    [ {LOWER: 'antennal'}, {LOWER: 'lobe'} ],
    [ {LOWER: 'right'}, {LOWER: 'antennal'}, {LOWER: 'lobe'} ],
    [ {LOWER: 'left'}, {LOWER: 'antennal'}, {LOWER: 'lobe'} ],
    [ {LOWER: 'right'}, {LOWER: 'al'} ],
    [ {LOWER: 'left'}, {LOWER: 'al'} ],
    [ {LOWER: 'al_r'} ],
    [ {LOWER: 'al_l'} ],
    [ {LOWER: 'al'} ]
] )
# TODO: Support other (valid) spellings of terms, e.g. "centre" as "center"
#       Could do this with a distance metric (but not complain to the user).
nlp.matcher.add( 'AMMC', 'NEUROPIL', {}, [
    [ {LOWER: 'antennal'}, {LOWER: 'mechanosensory'}, {LOWER: 'and'}, {LOWER: 'motor'}, {LOWER: 'center'} ],
    [ {LOWER: 'right'}, {LOWER: 'antennal'}, {LOWER: 'mechanosensory'}, {LOWER: 'and'}, {LOWER: 'motor'}, {LOWER: 'center'} ],
    [ {LOWER: 'left'}, {LOWER: 'antennal'}, {LOWER: 'mechanosensory'}, {LOWER: 'and'}, {LOWER: 'motor'}, {LOWER: 'center'} ],
    [ {LOWER: 'ammc_r'} ],
    [ {LOWER: 'ammc_l'} ],
    [ {LOWER: 'ammc'} ]
] )
nlp.matcher.add( 'CCP', 'NEUROPIL', {}, [
    [ {LOWER: 'caudalcentral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'caudalcentral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'caudalcentral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'ccp'} ],
    [ {LOWER: 'left'}, {LOWER: 'ccp'} ],
    [ {LOWER: 'ccp_r'} ],
    [ {LOWER: 'ccp_l'} ],
    [ {LOWER: 'ccp'} ]
] )
nlp.matcher.add( 'CMP', 'NEUROPIL', {}, [
    [ {LOWER: 'caudalmedial'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'caudalmedial'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'caudalmedial'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'cmp'} ],
    [ {LOWER: 'left'}, {LOWER: 'cmp'} ],
    [ {LOWER: 'cmp_r'} ],
    [ {LOWER: 'cmp_l'} ],
    [ {LOWER: 'cmp'} ]
] )
nlp.matcher.add( 'CVLP', 'NEUROPIL', {}, [
    [ {LOWER: 'caudal'}, {LOWER: 'ventrolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'caudal'}, {LOWER: 'ventrolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'caudal'}, {LOWER: 'ventrolater'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'cvlp'} ],
    [ {LOWER: 'left'}, {LOWER: 'cvlp'} ],
    [ {LOWER: 'cvlp_r'} ],
    [ {LOWER: 'cvlp_l'} ],
    [ {LOWER: 'cvlp'} ]
] )
nlp.matcher.add( 'DLP', 'NEUROPIL', {}, [
    [ {LOWER: 'dorsolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'dorsolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'dorsolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'dlp'} ],
    [ {LOWER: 'left'}, {LOWER: 'dlp'} ],
    [ {LOWER: 'dlp_r'} ],
    [ {LOWER: 'dlp_l'} ],
    [ {LOWER: 'dlp'} ]
] )
nlp.matcher.add( 'DMP', 'NEUROPIL', {}, [
    [ {LOWER: 'dorsomedial'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'dorsomedial'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'dorsomedial'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'dmp'} ],
    [ {LOWER: 'left'}, {LOWER: 'dmp'} ],
    [ {LOWER: 'dmp_r'} ],
    [ {LOWER: 'dmp_l'} ],
    [ {LOWER: 'dmp'} ],
    [ {LOWER: 'right'}, {LOWER: 'icl'} ],
    [ {LOWER: 'left'}, {LOWER: 'icl'} ],
    [ {LOWER: 'icl_r'} ],
    [ {LOWER: 'icl_l'} ],
    [ {LOWER: 'icl'} ]
] )
nlp.matcher.add( 'EB', 'NEUROPIL', {}, [
    [ {LOWER: 'ellipsoid'}, {LOWER: 'body'} ],
    [ {LOWER: 'right'}, {LOWER: 'ellipsoid'}, {LOWER: 'body'} ],
    [ {LOWER: 'left'}, {LOWER: 'ellipsoid'}, {LOWER: 'body'} ],
    [ {LOWER: 'eb_r'} ],
    [ {LOWER: 'eb_l'} ],
    [ {LOWER: 'eb'} ]
] )
nlp.matcher.add( 'FSPP', 'NEUROPIL', {}, [
    [ {LOWER: 'frontal'}, {LOWER: 'superpeduncular'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'frontal'}, {LOWER: 'superpeduncular'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'frontal'}, {LOWER: 'superpeduncular'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'fspp'} ],
    [ {LOWER: 'left'}, {LOWER: 'fspp'} ],
    [ {LOWER: 'fspp_r'} ],
    [ {LOWER: 'fspp_l'} ],
    [ {LOWER: 'fspp'} ]
] )
nlp.matcher.add( 'IDFP', 'NEUROPIL', {}, [
    [ {LOWER: 'inferior'}, {LOWER: 'dorsofrontal'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'inferior'}, {LOWER: 'dorsofrontal'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'inferior'}, {LOWER: 'dorsofrontal'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'idfp'} ],
    [ {LOWER: 'left'}, {LOWER: 'idfp'} ],
    [ {LOWER: 'idfp_r'} ],
    [ {LOWER: 'idfp_l'} ],
    [ {LOWER: 'idfp'} ]
] )
nlp.matcher.add( 'IDLP', 'NEUROPIL', {}, [
    [ {LOWER: 'inferior'}, {LOWER: 'dorsolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'inferior'}, {LOWER: 'dorsolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'inferior'}, {LOWER: 'dorsolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'idlp'} ],
    [ {LOWER: 'left'}, {LOWER: 'idlp'} ],
    [ {LOWER: 'idlp_r'} ],
    [ {LOWER: 'idlp_l'} ],
    [ {LOWER: 'idlp'} ]
] )
nlp.matcher.add( 'LAT', 'NEUROPIL', {}, [
    [ {LOWER: 'lat'} ],
    [ {LOWER: 'right'}, {LOWER: 'lat'} ],
    [ {LOWER: 'left'}, {LOWER: 'lat'} ],
    [ {LOWER: 'lat_r'} ],
    [ {LOWER: 'lat_l'} ]
] )
nlp.matcher.add( 'LH', 'NEUROPIL', {}, [
    [ {LOWER: 'lateral'}, {LOWER: 'horn'} ],
    [ {LOWER: 'right'}, {LOWER: 'lateral'}, {LOWER: 'horn'} ],
    [ {LOWER: 'left'}, {LOWER: 'lateral'}, {LOWER: 'horn'} ],
    [ {LOWER: 'right'}, {LOWER: 'lh'} ],
    [ {LOWER: 'left'}, {LOWER: 'lh'} ],
    [ {LOWER: 'lh_r'} ],
    [ {LOWER: 'lh_l'} ],
    [ {LOWER: 'lh'} ]
] )
nlp.matcher.add( 'LOB', 'NEUROPIL', {}, [
    [ {LOWER: 'lobula'} ],
    [ {LOWER: 'right'}, {LOWER: 'lobula'} ],
    [ {LOWER: 'left'}, {LOWER: 'lobula'} ],
    [ {LOWER: 'right'}, {LOWER: 'lob'} ],
    [ {LOWER: 'left'}, {LOWER: 'lob'} ],
    [ {LOWER: 'right'}, {LOWER: 'lo'} ],
    [ {LOWER: 'left'}, {LOWER: 'lo'} ],
    [ {LOWER: 'lob_r'} ],
    [ {LOWER: 'lob_l'} ],
    [ {LOWER: 'lo_r'} ],
    [ {LOWER: 'lo_l'} ],
    [ {LOWER: 'lob'} ],
    [ {LOWER: 'lo'} ]
] )
nlp.matcher.add( 'LOP', 'NEUROPIL', {}, [
    [ {LOWER: 'lobula'}, {LOWER: 'plate'} ],
    [ {LOWER: 'right'}, {LOWER: 'lobula'}, {LOWER: 'plate'} ],
    [ {LOWER: 'left'}, {LOWER: 'lobula'}, {LOWER: 'plate'} ],
    [ {LOWER: 'right'}, {LOWER: 'lop'} ],
    [ {LOWER: 'left'}, {LOWER: 'lop'} ],
    [ {LOWER: 'lop_r'} ],
    [ {LOWER: 'lop_l'} ],
    [ {LOWER: 'lop'} ]
] )
nlp.matcher.add( 'MB', 'NEUROPIL', {}, [
    [ {LOWER: 'mushroom'}, {LOWER: 'body'} ],
    [ {LOWER: 'right'}, {LOWER: 'mushroom'}, {LOWER: 'body'} ],
    [ {LOWER: 'left'}, {LOWER: 'mushroom'}, {LOWER: 'body'} ],
    [ {LOWER: 'right'}, {LOWER: 'mb'} ],
    [ {LOWER: 'left'}, {LOWER: 'mb'} ],
    [ {LOWER: 'mb_r'} ],
    [ {LOWER: 'mb_l'} ],
    [ {LOWER: 'mb'} ]
] )
nlp.matcher.add( 'MED', 'NEUROPIL', {}, [
    [ {LOWER: 'medulla'} ],
    [ {LOWER: 'right'}, {LOWER: 'medulla'} ],
    [ {LOWER: 'left'}, {LOWER: 'medulla'} ],
    [ {LOWER: 'right'}, {LOWER: 'med'} ],
    [ {LOWER: 'left'}, {LOWER: 'med'} ],
    [ {LOWER: 'right'}, {LOWER: 'me'} ],
    [ {LOWER: 'left'}, {LOWER: 'me'} ],
    [ {LOWER: 'med_r'} ],
    [ {LOWER: 'med_l'} ],
    [ {LOWER: 'me_r'} ],
    [ {LOWER: 'me_l'} ],
    [ {LOWER: 'med'} ],
    [ {LOWER: 'me'} ]
] )
nlp.matcher.add( 'LAM', 'NEUROPIL', {}, [
    [ {LOWER: 'lamina'} ],
    [ {LOWER: 'right'}, {LOWER: 'lamina'} ],
    [ {LOWER: 'left'}, {LOWER: 'lamina'} ],
    [ {LOWER: 'right'}, {LOWER: 'lam'} ],
    [ {LOWER: 'left'}, {LOWER: 'lam'} ],
    [ {LOWER: 'right'}, {LOWER: 'la'} ],
    [ {LOWER: 'left'}, {LOWER: 'la'} ],
    [ {LOWER: 'lam_r'} ],
    [ {LOWER: 'lam_l'} ],
    [ {LOWER: 'la_r'} ],
    [ {LOWER: 'la_l'} ],
    [ {LOWER: 'lam'} ],
    [ {LOWER: 'la'} ]
] )
nlp.matcher.add( 'NOD', 'NEUROPIL', {}, [
    [ {LOWER: 'noduli'} ],
    [ {LOWER: 'right'}, {LOWER: 'noduli'} ],
    [ {LOWER: 'left'}, {LOWER: 'noduli'} ],
    [ {LOWER: 'right'}, {LOWER: 'nod'} ],
    [ {LOWER: 'left'}, {LOWER: 'nod'} ],
    [ {LOWER: 'right'}, {LOWER: 'no'} ],
    [ {LOWER: 'left'}, {LOWER: 'no'} ],
    [ {LOWER: 'nod_r'} ],
    [ {LOWER: 'nod_l'} ],
    [ {LOWER: 'no_r'} ],
    [ {LOWER: 'no_l'} ],
    [ {LOWER: 'nod'} ],
    [ {LOWER: 'no'} ]
] )
nlp.matcher.add( 'OG', 'NEUROPIL', {}, [
    [ {LOWER: 'optic'}, {LOWER: 'glomerulus'} ],
    [ {LOWER: 'right'}, {LOWER: 'optic'}, {LOWER: 'glomerulus'} ],
    [ {LOWER: 'left'}, {LOWER: 'optic'}, {LOWER: 'glomerulus'} ],
    [ {LOWER: 'right'}, {LOWER: 'og'} ],
    [ {LOWER: 'left'}, {LOWER: 'og'} ],
    [ {LOWER: 'og_r'} ],
    [ {LOWER: 'og_l'} ],
    [ {LOWER: 'og'} ]
] )
nlp.matcher.add( 'OPTU', 'NEUROPIL', {}, [
    [ {LOWER: 'optic'}, {LOWER: 'tubercle'} ],
    [ {LOWER: 'right'}, {LOWER: 'optic'}, {LOWER: 'tubercle'} ],
    [ {LOWER: 'left'}, {LOWER: 'optic'}, {LOWER: 'tubercle'} ],
    [ {LOWER: 'right'}, {LOWER: 'optu'} ],
    [ {LOWER: 'left'}, {LOWER: 'optu'} ],
    [ {LOWER: 'optu_r'} ],
    [ {LOWER: 'optu_l'} ],
    [ {LOWER: 'optu'} ]
] )
nlp.matcher.add( 'PAN', 'NEUROPIL', {}, [
    [ {LOWER: 'proximal'}, {LOWER: 'antennal'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'proximal'}, {LOWER: 'antennal'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'proximal'}, {LOWER: 'antennal'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'pan'} ],
    [ {LOWER: 'left'}, {LOWER: 'pan'} ],
    [ {LOWER: 'pan_r'} ],
    [ {LOWER: 'pan_l'} ],
    [ {LOWER: 'pan'} ]
] )
nlp.matcher.add( 'PB', 'NEUROPIL', {}, [
    [ {LOWER: 'protocerebral'}, {LOWER: 'bridge'} ],
    [ {LOWER: 'right'}, {LOWER: 'protocerebral'}, {LOWER: 'bridge'} ],
    [ {LOWER: 'left'}, {LOWER: 'protocerebral'}, {LOWER: 'bridge'} ],
    [ {LOWER: 'right'}, {LOWER: 'pcb'} ],
    [ {LOWER: 'left'}, {LOWER: 'pcb'} ],
    [ {LOWER: 'right'}, {LOWER: 'pb'} ],
    [ {LOWER: 'left'}, {LOWER: 'pb'} ],
    [ {LOWER: 'pcb_r'} ],
    [ {LOWER: 'pcb_l'} ],
    [ {LOWER: 'pb_r'} ],
    [ {LOWER: 'pb_l'} ],
    [ {LOWER: 'pcb'} ],
    [ {LOWER: 'pb'} ]
] )
nlp.matcher.add( 'SDFP', 'NEUROPIL', {}, [
    [ {LOWER: 'superior'}, {LOWER: 'dorsofrontal'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'superior'}, {LOWER: 'dorsofrontal'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'superior'}, {LOWER: 'dorsofrontal'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'sdfp'} ],
    [ {LOWER: 'left'}, {LOWER: 'sdfp'} ],
    [ {LOWER: 'sdfp_r'} ],
    [ {LOWER: 'sdfp_l'} ],
    [ {LOWER: 'sdfp'} ]
] )
nlp.matcher.add( 'SOG', 'NEUROPIL', {}, [
    [ {LOWER: 'subesophageal'}, {LOWER: 'ganglion'} ],
    [ {LOWER: 'right'}, {LOWER: 'subesophageal'}, {LOWER: 'ganglion'} ],
    [ {LOWER: 'left'}, {LOWER: 'subesophageal'}, {LOWER: 'ganglion'} ],
    [ {LOWER: 'right'}, {LOWER: 'sog'} ],
    [ {LOWER: 'left'}, {LOWER: 'sog'} ],
    [ {LOWER: 'sog_r'} ],
    [ {LOWER: 'sog_l'} ],
    [ {LOWER: 'sog'} ]
] )
nlp.matcher.add( 'SPP', 'NEUROPIL', {}, [
    [ {LOWER: 'superpeduncular'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'superpeduncular'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'superpeduncular'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'spp'} ],
    [ {LOWER: 'left'}, {LOWER: 'spp'} ],
    [ {LOWER: 'spp_r'} ],
    [ {LOWER: 'spp_l'} ],
    [ {LOWER: 'spp'} ]
] )
# TODO: And support supporting of hyphens, etc...
nlp.matcher.add( 'FB', 'NEUROPIL', {}, [
    [ {LOWER: 'fanshaped'}, {LOWER: 'body'} ],
    [ {LOWER: 'right'}, {LOWER: 'fanshaped'}, {LOWER: 'body'} ],
    [ {LOWER: 'left'}, {LOWER: 'fanshaped'}, {LOWER: 'body'} ],
    [ {LOWER: 'right'}, {LOWER: 'fb'} ],
    [ {LOWER: 'left'}, {LOWER: 'fb'} ],
    [ {LOWER: 'fb_r'} ],
    [ {LOWER: 'fb_l'} ],
    [ {LOWER: 'fb'} ]
] )
nlp.matcher.add( 'VLP', 'NEUROPIL', {}, [
    [ {LOWER: 'ventrolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'ventrolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'ventrolateral'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'vlp'} ],
    [ {LOWER: 'left'}, {LOWER: 'vlp'} ],
    [ {LOWER: 'vlp_r'} ],
    [ {LOWER: 'vlp_l'} ],
    [ {LOWER: 'vlp'} ]
] )
nlp.matcher.add( 'VMP', 'NEUROPIL', {}, [
    [ {LOWER: 'ventromedial'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'ventromedial'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'left'}, {LOWER: 'ventromedial'}, {LOWER: 'protocerebrum'} ],
    [ {LOWER: 'right'}, {LOWER: 'vmp'} ],
    [ {LOWER: 'left'}, {LOWER: 'vmp'} ],
    [ {LOWER: 'vmp_r'} ],
    [ {LOWER: 'vmp_l'} ],
    [ {LOWER: 'vmp'} ]
] )

from quepy.tagger import Word
from quepy.encodingpolicy import assert_valid_encoding

import logging
log = logging.getLogger( 'quepy.spacytagger' )

import re
# TODO: If this is used later on, how will it affect our spell-checking?
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

    for ent in doc.ents:
        if ent.label_ == 'NEUROPIL':
            ent.merge( u'NNP', ent.text, u'NEUROPIL' )

    words = [ Word(x.text, x.lemma_, x.tag_) for x in doc ]
    # TODO: Remove Words that have a POS tag not in the PTB? Quepy will complain later if any found.
    #       e.g. a hypen can be its own token, with .tag_ "HYPH"; spaces are "SP".
    # TODO: Check if there are instances when spaCy couldn't lemmatize.
    #       Maybe just output token.lower() in those cases?
    # TODO: Use x.tag_ for (at least some) POSes? .tag_ is the "fine-grained" POS.

    # The following is only for logging purposes; if necessary, it could be removed for production
    log.info( ' '.join([ t.text +'['+ str(t.i) +']' for t in doc ]) )
    # In particular, the next few lines are (arguably) "nit-picky"...
    indent = "  "
    longest = max( len(t.text) for t in doc )
    column = (len(doc) - 1) * len(indent) + longest + 2
    wout = '{:'+ str(column) +'}| '
    #wout = "{:35}"
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

    #log.info( 'Words: '+ str(words) )
    log.info( 'Ents:  '+ str(doc.ents) )
    log.info( 'NPs:   '+ str(list(doc.noun_chunks)) )

    return words
