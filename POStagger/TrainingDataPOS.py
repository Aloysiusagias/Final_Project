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

from scipy.sparse import dok

df = pd.read_csv('readytfidf3.csv')
# print(df['Normal'])

file = open('indonesian_ngram_pos_tag.pickle', 'rb')
ngram_tagger = pickle.load(file)
file.close()

# def word_tokenize_wrapper(text):
#     return word_tokenize(text)
testingfix = []
for index, row in df.iterrows():
    # print(row['Normal'])
    testingfix.append(row['Normal'])

# print(testingfix)

d ={}
j = 0
for i in testingfix:
    i = i.split()
    #print("N-gram tagger")
    postag = ngram_tagger.tag(i)
    #print (postag)
    dictcorpus=dict(postag)
    d[j] = {}
    d[j]=dictcorpus
    j+=1

# print(d)

# df['Normal'] = df['Normal'].apply(tagger)
# print(df['Normal'].iloc(0)[1])


#TF
# benci=[]
# bencinew=[]
# with open('indikasi.csv') as csvfile:
#     readCSV = csv.reader(csvfile)
#     for i in readCSV:
#         benci.insert(len(benci),i)

# for i in benci:
#     for j in i :
#         bencinew.append(j)

# worddict= dict.fromkeys(bencinew, 0)

# # print(worddict)

# def satu(d):
#     k=0
#     dictbenci={}
#     for i in d: 
#         dictbenci[k]={}
#         dictbenci[k]=worddict
#         k+=1
#     return(dictbenci)
# dictbenci = df['Normal'].apply(satu)
# # print(dictbenci)

# # print(df['Normal'])
# # d = df['Normal'].iloc(0)[0]
# # print(d)
# # for y in d.keys():
# #     print(y)
# dictbenci = dictbenci[0]
# def dua(d):
#     dictbencinew={}
#     l=0
#     for x in d.keys():
#         dictbenci[x]=dict.fromkeys(dictbenci[x],0)
#         for y in d[x].keys():       
#             for word in bencinew:
#                 if(y == word):
#                     dictbenci[x][word]+=1
#                     # print("Masuk\n\n\n\n")
#             dictbencinew[l]={}
#             dictbencinew[l]=dictbenci[x]
#         l+=1
#     return(dictbencinew)
# dictbencinew = df['Normal'].apply(dua)

# # print(df['Normal'])
# # print(dictbencinew.iloc(0)[1])

# # print(bencinew)
# # print(dictbencinew[0][0]['hijau'])

# for index, row in df.iterrows():
#     # print(row['Normal'])
#     d = row['Normal']
#     for x in d.keys():
#         for y in d[x].keys():
#             for word in bencinew:    
#                 if(y in word and (d[x][y] == 'NN' or d[x][y] =='NNP' or d[x][y]=='NNG' or d[x][y]=='VBI' or d[x][y]=='VBT')):
#                     dictbencinew[index][x][word]=dictbencinew[index][x][word]*5
#                 elif(y in word and (d[x][y] == 'JJ' or d[x][y]=='RB')):
#                     dictbencinew[index][x][word]=dictbencinew[index][x][word]*3
#                 else :
#                     dictbencinew[index][x][word]=dictbencinew[index][x][word]*1

# # print(dictbencinew.iloc(0)[1])

# def tiga(dictbencinew):
#     jumlahdictbenci=0
#     dictbencitf={}
#     z=0
#     for x in dictbencinew.keys():
#         for y in dictbencinew[x].keys():
#             jumlahdictbenci=jumlahdictbenci+dictbencinew[x][y]
#             dictbencitf[z]={}
#         dictbencitf[z]=jumlahdictbenci
#         z+=1
#         jumlahdictbenci=0
    
#     for x in dictbencinew.keys():
#         for y in dictbencinew[x].keys():
#           if(dictbencinew[x][y]>0):
#             dictbencinew[x][y]=dictbencinew[x][y]/dictbencitf[x]

#     return(dictbencinew)

# dictbencinew = dictbencinew.apply(tiga)
# # print(dictbencinew.iloc(0)[1])

# #IDF
# def empat(d):
#     dictidf=dict.fromkeys(bencinew,0)
#     N = len(testingfix)
#     for x in d.keys():
#         for y in d[x].keys():       
#             for word in bencinew:
#                 if(y == word):
#                     dictidf[word]+=1
#     return(dictidf)


#TF
benci=[]
bencinew=[]
with open('indikasi.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for i in readCSV:
        benci.insert(len(benci),i)

for i in benci:
    for j in i :
        bencinew.append(j)
worddict= dict.fromkeys(bencinew, 0)
k=0
dictbenci={}
for i in d: 
    dictbenci[k]={}
    dictbenci[k]=worddict
    k+=1
dictbencinew={}
l=0
for x in d.keys():
    dictbenci[x]=dict.fromkeys(dictbenci[x],0)
    for y in d[x].keys():       
        for word in bencinew:
            if(y == word):
                dictbenci[x][word]+=1
        dictbencinew[l]={}
        dictbencinew[l]=dictbenci[x]
    l+=1
for x in d.keys():
    for y in d[x].keys():
        for word in bencinew:    
            if(y in word and (d[x][y] == 'NN' or d[x][y] =='NNP' or d[x][y]=='NNG' or d[x][y]=='VBI' or d[x][y]=='VBT')):
                dictbencinew[x][word]=dictbencinew[x][word]*5
            elif(y in word and (d[x][y] == 'JJ' or d[x][y]=='RB')):
                dictbencinew[x][word]=dictbencinew[x][word]*3
            else :
                dictbencinew[x][word]=dictbencinew[x][word]*1
jumlahdictbenci=0
dictbencitf={}
z=0
for x in dictbencinew.keys():
    for y in dictbencinew[x].keys():
        jumlahdictbenci=jumlahdictbenci+dictbencinew[x][y]
        dictbencitf[z]={}
    dictbencitf[z]=jumlahdictbenci
    z+=1
    jumlahdictbenci=0

for x in dictbencinew.keys():
    for y in dictbencinew[x].keys():
          if(dictbencinew[x][y]>0):
            dictbencinew[x][y]=dictbencinew[x][y]/dictbencitf[x]

#IDF
dictidf=dict.fromkeys(bencinew,0)
N = len(testingfix)
for x in d.keys():
    for y in d[x].keys():       
        for word in bencinew:
            if(y == word):
                dictidf[word]+=1
for x in dictidf.keys():
    dictidf[x]=1 + math.log10((1+N)/(1+dictidf[x]))
for x in dictbencinew.keys():
    for y in dictbencinew[x].keys():
        dictbencinew[x][y]=dictbencinew[x][y]*dictidf[y]
        
#Normalisasi
jumlahnorm=0
dictnorm={}
e=0
for x in dictbencinew.keys():
    for y in dictbencinew[x].keys():
        jumlahnorm=jumlahnorm+(dictbencinew[x][y]*dictbencinew[x][y])
        dictnorm[e]={}
    dictnorm[e]=math.sqrt(jumlahnorm)
    e+=1
    jumlahnorm=0
for x in dictbencinew.keys():
    for y in dictbencinew[x].keys():
        if(dictbencinew[x][y]>0):
            dictbencinew[x][y]=dictbencinew[x][y]/dictnorm[x]
    
df = pd.DataFrame.from_dict(dictbencinew, orient='index')

predict=df.values.tolist()

print(predict)

df.to_csv('DataSiapPOS.csv')