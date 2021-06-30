import csv
from nltk.util import pr
from numpy import testing
import pandas as pd
import requests, json
import nltk
import re
import string
from nltk.tokenize import word_tokenize
import pickle
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import csv
import math



file = open('indonesian_ngram_pos_tag.pickle', 'rb')
ngram_tagger = pickle.load(file)
file.close()

testingfix = "bosan lihat lesu"
testingfix = testingfix.split(" ")
print(testingfix)
testingfix = [testingfix]

d ={}
j = 0
for i in testingfix:
    #print("N-gram tagger")
    postag = ngram_tagger.tag(i)
    #print (postag)
    dictcorpus=dict(postag)
    d[j] = {}
    d[j]=dictcorpus
    j+=1

print(d)