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
import csv
import pickle

# indikasi = []
# a = []
# with open('indikasi.csv') as csvfile:
#     readCSV = csv.reader(csvfile)
#     for i in readCSV:
#         a.insert(len(indikasi),i[0])
#     indikasi.append(a)

# print(indikasi)

# file = open('indonesian_ngram_pos_tag.pickle', 'rb')
# ngram_tagger = pickle.load(file)
# file.close()

# d ={}
# j = 0
# for i in indikasi:
#     # print(i)
#     postag = ngram_tagger.tag(i)
#     # print (postag)
#     dictcorpus=dict(postag)
#     d[j] = {}
#     d[j]=dictcorpus
#     j+=1

# print(d)
stop = []
a = []
with open('stop.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for i in readCSV:
        a.insert(len(stop),i[0])
    stop.append(a)
    
stop = stop[0]
list_stopwords = set(stopwords.words('indonesian'))
for a in stop:
    list_stopwords.add(a)
print(list_stopwords)