# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

import importlib
import re

import spacy
from spacy.attrs import LOWER

from quepy import settings
from quepy.encodingpolicy import assert_valid_encoding

import logging
logger = logging.getLogger("quepy.tagger")
PENN_TAGSET = set(u"$ `` '' ( ) , -- . : CC CD DT EX FW IN JJ JJR JJS LS MD "
                  "NN NNP NNPS NNS PDT POS PRP PRP$ RB RBR RBS RP SYM TO UH "
                  "VB VBD VBG VBN VBP VBZ WDT WP WP$ WRB".split())


class TaggingError(Exception):
    """
    Error parsing tagger's output.
    """
    pass


class Word(object):
    """
    Representation of a tagged word.
    Contains *token*, *lemma*, *pos tag* and optionally a *probability* of
    that tag.
    """
    _encoding_attrs = u"token lemma pos".split()
    _attrs = _encoding_attrs + [u"prob"]

    def __init__(self, token, lemma=None, pos=None, prob=None):
        self.pos = pos
        self.prob = prob
        self.lemma = lemma
        self.token = token

    def __setattr__(self, name, value):
        if name in self._encoding_attrs and value is not None:
            assert_valid_encoding(value)
        object.__setattr__(self, name, value)

    def __unicode__(self):
        attrs = (getattr(self, name, u"-") for name in self._attrs)
        return u"|".join(str(x) for x in attrs)

    def __repr__(self):
        return unicode(self)


def get_tagger(app_name):
    """
    Return a tagging function given some app settings.
    `Settings` is the settings module of an app.
    The returned value is a function that receives a unicode string and returns
    a list of `Word` instances.
    """

    # TODO: Decide approach
    #parser = getattr( settings.PARSER, None )
    #if parser == "spaCy":
    if settings.PARSER == 'spaCy':
        from neuroarch_nlp.data import colors_values
        defaults = importlib.import_module('{}.defaults'.format(app_name))
        neuropils = getattr(defaults, 'neuropils')
        subregions = getattr(defaults, 'subregions')
        nlp = spacy.load('en')

        # Go through the accepted (English) string representations of neuropil names
        # and add the multi-word names to spaCy's rule-based Matcher, so we can merge
        # each name as a single token (later), which will slightly simplify the grammar
        for db_rep, string_reps in neuropils:
            for string in string_reps:
                lexes = string.split()
                if len( lexes ) > 1:
                    # NOTE: The first parameter, the ID, could be specified as the "canonical" neuropil name
                    nlp.matcher.add_pattern( 'NEUROPIL',
                                             [ {LOWER: lex.lower()} for lex in lexes ],
                                             label='NEUROPIL' )

        for phrase in subregions.keys() + colors_values.keys():
            phrase = phrase.split()
            if len( phrase ) > 1:
                nlp.matcher.add_pattern( 'SUBREGION',
                                         [ {LOWER: lex.lower()} for lex in phrase ],
                                         label='SUBREGION' )

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
                     for ent_id, label_id, start, end in nlp.matcher( doc ) ]
            for ent_id, label_id, span in spans:
                span.merge( label=label_id, tag='NNP' if label_id else span.root.tag_ )

            # tag_ is the "fine-grained" POS
            words = [ Word(x.text, x.lemma_, x.tag_) for x in doc ]

            # The following is only for logging purposes; if necessary, it could be removed for production
            logger.info( ' '.join([ t.text +'['+ str(t.i) +']' for t in doc ]) )
            indent = "  "
            longest = max( len(t.text) for t in doc )
            column = (len(doc) - 1) * len(indent) + longest + 2
            wout = '{:'+ str(column) +'}| '
            def trav_tree( indents, node ):
                logger.info( wout.format((indent * indents) + node.text) + ', '.join(
                    [ str(x) for x in [
                        node.i, node.is_oov, node.lemma_, node.tag_, \
                        "<-"+ str(node.left_edge), str(node.right_edge) +"->"] ]) )
                for el in node.children:
                    # NOTE: Could also change display based on node.lefts and node.rights
                    trav_tree( indents + 1, el )
            for sent in doc.sents:
                trav_tree( 0, sent.root )
            logger.info( 'Ents:  '+ str(doc.ents) )
            logger.info( 'NPs:   '+ str(list(doc.noun_chunks)) )

            return words
        tagger_function = run_spacytagger
    else:
        from quepy.nltktagger import run_nltktagger
        tagger_function = lambda x: run_nltktagger(x, settings.NLTK_DATA_PATH)

    def wrapper(string):
        assert_valid_encoding(string)
        words = tagger_function(string)
        for word in words:
            if word.pos not in PENN_TAGSET:
                logger.warning("Tagger emmited a non-penn "
                               "POS tag {!r}".format(word.pos))
        return words
    return wrapper
