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
from spacy.matcher import Matcher
from spacy.symbols import ORTH
from spacy.util import filter_spans
import numpy as np

from quepy import settings
from quepy.encodingpolicy import assert_valid_encoding

import logging
logger = logging.getLogger("quepy.tagger")
PENN_TAGSET = set("$ `` '' ( ) , -- . : CC CD DT EX FW IN JJ JJR JJS LS MD "
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
    _encoding_attrs = "token lemma pos".split()
    _attrs = _encoding_attrs + ["prob"]

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
        attrs = (getattr(self, name, "-") for name in self._attrs)
        return "|".join(str(x) for x in attrs)

    def __repr__(self):
        return self.__unicode__()


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
        arborization_regions = getattr(defaults, 'arborization_regions')
        subregions = getattr(defaults, 'subregions')
        neuron_types = getattr(defaults, 'neuron_types')
        
        nlp = spacy.load('en_core_web_sm')
        matcher = Matcher(nlp.vocab)
        vocab = nlp.vocab

        vector_data = {}

        neuron_type_patterns = []
        for n in neuron_types:
            lexes = n.split()
            for lex in lexes:
                if lex not in vocab:
                    vector_data[lex] = np.random.uniform(-1, 1, (300,)).astype(np.float32)
            if len(lexes) > 1:
                neuron_type_patterns.append([ {LOWER: lex.lower()} for lex in lexes ])
        matcher.add( 'NEURONTYPE', neuron_type_patterns)

        neuropil_patterns = []
        for db_rep, string_reps in neuropils:
            for string in string_reps:
                lexes = string.split()
                for lex in lexes:
                    if lex not in vocab:
                        vector_data[lex] = np.random.uniform(-1, 1, (300,)).astype(np.float32)
                    
                if len( lexes ) > 1:
                    neuropil_patterns.append([ {LOWER: lex.lower()} for lex in lexes ])

        matcher.add( 'NEUROPIL', neuropil_patterns)
                
        subregion_patterns = []
        for db_rep, string_reps in arborization_regions:
            for string in string_reps:
                lexes = string.split()
                for lex in lexes:
                    if lex not in vocab:
                        vector_data[lex] = np.random.uniform(-1, 1, (300,)).astype(np.float32)
                    
                if len( lexes ) > 1:
                    subregion_patterns.append([ {LOWER: lex.lower()} for lex in lexes ])

        for phrase in subregions:
            phrase = phrase.split()
            for lex in phrase:
                if lex not in vocab:
                    vector_data[lex] = np.random.uniform(-1, 1, (300,)).astype(np.float32)
            if len( phrase ) > 1:
                subregion_patterns.append([ {LOWER: lex.lower()} for lex in phrase ])
        matcher.add( 'SUBREGION', subregion_patterns)

        color_patterns = []
        for phrase in colors_values:
            phrase = phrase.split()
            for lex in phrase:
                if lex not in vocab:
                    vector_data[lex] = np.random.uniform(-1, 1, (300,)).astype(np.float32)
            if len( phrase ) > 1:
                color_patterns.append([ {LOWER: lex.lower()} for lex in phrase ])
        matcher.add( 'COLOR', color_patterns)

        for word, vector in vector_data.items():
            vocab.set_vector(word, vector)
            special_case = [{ORTH: word}]
            nlp.tokenizer.add_special_case(word, special_case)
            

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

            spans = [doc[start:end]
                for match_id, start, end in matcher( doc ) ]
            filtered = filter_spans(spans)
            with doc.retokenize() as retokenizer:
                for span in filtered:
                    retokenizer.merge(span)
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
