import string 
import re #regex library

# import word_tokenize & FreqDist from NLTK
from nltk.tokenize import word_tokenize 
from nltk.probability import FreqDist

import pandas as pd 
import numpy as np
import os
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def Preprocessing(text):
    #Case Folding
    text = text.lower()
    # ------ Tokenizing ---------

    # remove tab, new line, ans back slice
    text = text.replace('\\t'," ").replace('\\n'," ").replace('\\u'," ").replace('\\',"")
    # remove non ASCII (emoticon, chinese word, .etc)
    text = text.encode('ascii', 'replace').decode('ascii')
    # remove mention, link, hashtag
    text = ' '.join(re.sub("([@#][A-Za-z0-9]+)|(\w+:\/\/\S+)"," ", text).split())
    # remove incomplete URL
    text = text.replace("http://", " ").replace("https://", " ")

    #remove number
    text = re.sub(r"\d+", "", text)

    #remove punctuation
    text = text.translate(str.maketrans(string.punctuation,"                                "))

    #remove whitespace leading & trailing
    text = text.strip()

    #remove multiple whitespace into single whitespace
    text = re.sub('\s+',' ',text)

    # remove single char
    text = re.sub(r"\b[a-zA-Z]\b", "", text)

    # NLTK word rokenize 
    text = word_tokenize(text)

    normalizad_word = pd.read_excel("../Normalisasi.xlsx")
    normalizad_word_dict = {}

    for index, row in normalizad_word.iterrows():
        if row[0] not in normalizad_word_dict:
            normalizad_word_dict[row[0]] = row[1] 

    text = [normalizad_word_dict[term] if term in normalizad_word_dict else term for term in text]

    #get indonesia stop word
    list_stopwords = set(stopwords.words('indonesian'))
    #remove stopwords pada list token
    tokens_without_stopword = [word for word in text if not word in list_stopwords]
    text = tokens_without_stopword

    # create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    # stem
    output   = [stemmer.stem(token) for token in text]
    text = output
    return text