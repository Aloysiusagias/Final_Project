import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import ast
import numpy as np
import math


df = pd.read_csv('data.csv')

def convert_text_list(texts):
    texts = ast.literal_eval(texts)
    return [text for text in texts]

df['isi_list'] = df['isi'].apply(convert_text_list)
# print(df['isi_list'][0])

def unique(document):
    unique_word = set()
    for i in document:
        unique_word = unique_word.union(i)
    return(unique_word)

uw = unique(df['isi_list'])
# print(uw)

def numOfWords(docs, uw):
    numOfWord = [None] * len(docs)
    for i in range(len(docs)):
        numOfWord[i] = dict.fromkeys(uw, 0)
    counter = 0
    for news in docs: 
        for word in news:
            numOfWord[counter][word] += 1
        counter += 1
    return numOfWord

now = numOfWords(df['isi_list'], uw)
# dfn = pd.DataFrame(now)
# dfn.to_csv('tf_idf.csv')

def computeTF(dicts, bow):
    tfDict = [None] * len(bow)
    for i in range(len(dicts)):
        tfDict[i] = {}
        bagOfWordsCount = len(bow[i])
        for word, count in dicts[i].items():
            tfDict[i][word] = count/float(bagOfWordsCount)
    return tfDict

tfDict = computeTF(now, df['isi_list'])
# print(tfDict)

def computeIDF(documents):
    jumlahData = len(documents)
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    for word,val in idfDict.items():
        idfDict[word] = math.log(jumlahData / float(val))
    return idfDict

idfs = computeIDF(now)
# print(idfs)

def computeTFIDF(tf, idf):
    tfidf = [None] * len(tf)
    for i in range(len(tf)):
        tfidf[i] = {}
        for word, val in tf[i].items():
            tfidf[i][word] = val * idf[word]
    return tfidf

tfidf = computeTFIDF(tfDict, idfs)
# print(tfidf)
tfidf = pd.DataFrame(tfidf)
tfidf.to_csv('tf_idf.csv')