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
from nltk.tokenize import word_tokenize



file = open('indonesian_ngram_pos_tag.pickle', 'rb')
ngram_tagger = pickle.load(file)
file.close()

testingfix = "indonesia anjing"
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

kalimat = "indonesia anjing"

c = ngram_tagger.tag(word_tokenize(kalimat))
print("N-gram tagger")
print(c)

file = open('indonesian_classifier_pos_tag.pickle', 'rb')
classifier_tagger = pickle.load(file)
file.close()

print('\nClassifier tagger')
print(classifier_tagger.tag(word_tokenize(kalimat)))

file = open('indonesian_tnt_pos_tag.pickle', 'rb')
tnt_tagger = pickle.load(file)
file.close()

print('\nTnT tagger')
print(tnt_tagger.tag(word_tokenize(kalimat)))