import csv
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

testing = input("Masukkan data = ")
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
# d = d[0]
# print (d[0])


#TF
benci=[]
bencinew=[]
with open('katabenciunigram.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for i in readCSV:
        benci.insert(len(benci),i)

for i in benci:
    for j in i :
        bencinew.append(j)

worddict= dict.fromkeys(bencinew, 0)

# print(worddict)
# print(d[0])

k=0
dictbenci={}
for i in d: 
    dictbenci[k]={}
    dictbenci[k]=worddict
    k+=1
# print(dictbenci)
# print(d)
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
# print(dictbenci)

# print(d)
for x in d.keys():
    for y in d[x].keys():
        for word in bencinew:    
            if(y in word and (d[x][y] == 'NN' or d[x][y] =='NNP' or d[x][y]=='NNG' or d[x][y]=='VBI' or d[x][y]=='VBT')):
                dictbencinew[x][word]=dictbencinew[x][word]*5
            elif(y in word and (d[x][y] == 'JJ' or d[x][y]=='RB')):
                dictbencinew[x][word]=dictbencinew[x][word]*3
            else :
                dictbencinew[x][word]=dictbencinew[x][word]*1
# print(dictbencinew)

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
# print(dictbencitf)

for x in dictbencinew.keys():
    for y in dictbencinew[x].keys():
          if(dictbencinew[x][y]>0):
            dictbencinew[x][y]=dictbencinew[x][y]/dictbencitf[x]
# print(dictbencinew)

print(len(testingfix[0]))
#IDF
dictidf=dict.fromkeys(bencinew,0)
N = len(testingfix)
for x in d.keys():
    for y in d[x].keys():       
        for word in bencinew:
            if(y == word):
                dictidf[word]+=1
print(dictidf)
for x in dictidf.keys():
    dictidf[x]=1 + math.log10((1+N)/(1+dictidf[x]))
for x in dictbencinew.keys():
    for y in dictbencinew[x].keys():
        dictbencinew[x][y]=dictbencinew[x][y]*dictidf[y]
# print(dictbencinew)

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

# print(predict)