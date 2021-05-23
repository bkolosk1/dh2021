from googlesearch import search 
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import os
import pickle
import pandas as pd
from tqdm import tqdm
LANGUAGE = "english"
SENTENCES_COUNT = 50

def get_raw_doc(url):
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    return parser.document

def summarize_url(url):
    try:
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    except:
        return ["" * SENTENCES_COUNT]
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    outs = []
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        outs.append(str(sentence))
    return outs

x = pd.read_csv('all_wildfires.csv')
events = x['name'].to_list()
print(events)

outs = {}
for query in tqdm(events):
    findings_ = []
    outs[query] = []
    #query = "MV Wakashio oil spill"
    for j in search(query, num_results=10): 
        findings_=findings_+summarize_url(j)
        outs[query] = [] +  [" ".join(list(set(findings_)))]
        #outs[query] = get_raw_doc(j)
    print(outs[query])     

with open("text_data.pkl", "wb") as f:
    pickle.dump(outs, f)