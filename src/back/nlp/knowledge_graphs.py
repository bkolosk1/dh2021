import re
import sys
import pandas as pd
import bs4
import requests
import spacy
import pickle
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
from nltk.tokenize import sent_tokenize
from pyvis import network as net
from IPython.core.display import display, HTML
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from ..utils import utilities
nlp = spacy.load('en_core_web_sm')

def get_entities(sent):
    ## chunk 1
    ent1 = ""
    ent2 = ""
    prv_tok_dep = ""  # dependency tag of previous token in the sentence
    prv_tok_text = ""  # previous token in the sentence
    prefix = ""
    modifier = ""

    for tok in nlp(sent):
        ## chunk 2
        # if token is a punctuation mark then move on to the next token
        if tok.dep_ != "punct":
            # check: token is a compound word or not
            if tok.dep_ == "compound":
                prefix = tok.text
                # if the previous word was also a 'compound' then add the current word to it
                if prv_tok_dep == "compound":
                    prefix = prv_tok_text + " " + tok.text

            # check: token is a modifier or not
            if tok.dep_.endswith("mod") == True:
                modifier = tok.text
                # if the previous word was also a 'compound' then add the current word to it
                if prv_tok_dep == "compound":
                    modifier = prv_tok_text + " " + tok.text

            ## chunk 3
            if tok.dep_.find("subj") == True:
                ent1 = modifier + " " + prefix + " " + tok.text
                prefix = ""
                modifier = ""
                prv_tok_dep = ""
                prv_tok_text = ""

                ## chunk 4
            if tok.dep_.find("obj") == True:
                ent2 = modifier + " " + prefix + " " + tok.text

            ## chunk 5
            # update variables
            prv_tok_dep = tok.dep_
            prv_tok_text = tok.text
    return [ent1.strip(), ent2.strip()]

def get_relation(sent):

  doc = nlp(sent)

  # Matcher class object
  matcher = Matcher(nlp.vocab)

  #define the pattern
  pattern = [{'DEP':'ROOT'},
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},
            {'POS':'ADJ','OP':"?"}]

  matcher.add("matching_1", None, pattern)

  matches = matcher(doc)
  k = len(matches) - 1

  span = doc[matches[k][1]:matches[k][2]]

  return(span.text)

def generate_kg_html(texts,name, biggest=False):
    pairs = []
    relations = []
    for txt in txts['Camp fire']:
        for sent in sent_tokenize(txt):
            pairs.append(get_entities(sent))
            relations.append(get_relation(sent))
    source = [i[0] for i in pairs]
    target = [i[1] for i in pairs]
    kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})
    g=net.Network(height='500px', width='50%',heading='')
    for node in set(source+target):
        g.add_node(node)
    for source, target, label in zip(source,target, relations):
        g.add_edge(source, target, label=label)
    prefix = '../../data/KGs/'
    g.show(prefix+name+'.html')

def display_graphs(names):
    for name in names:
        generate_kg_html(names[name], name)
        display(HTML(name + '.html'))

if __name__ == '__main__':
    data = utilities.read_data_pickle(sys.argv[1])
    display_graphs(data)

