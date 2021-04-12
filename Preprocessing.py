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
DATA = pd.read_csv("Dataframe Siap/Dataframe Ready.csv")

DATA.head()

#Case Folding
print("Mulai Case Folding")
def case_folding(text):
  text = text.lower()
  return text
DATA['Pesan'] = DATA['Pesan'].apply(case_folding)

# ------ Tokenizing ---------
print("Mulai Tokenizing")
def remove_tweet_special(text):
    # remove tab, new line, ans back slice
    text = text.replace('\\t'," ").replace('\\n'," ").replace('\\u'," ").replace('\\',"")
    # remove non ASCII (emoticon, chinese word, .etc)
    text = text.encode('ascii', 'replace').decode('ascii')
    # remove mention, link, hashtag
    text = ' '.join(re.sub("([@#][A-Za-z0-9]+)|(\w+:\/\/\S+)"," ", text).split())
    # remove incomplete URL
    return text.replace("http://", " ").replace("https://", " ")
                
DATA['Hasil'] = DATA['Pesan'].apply(remove_tweet_special)

#remove number
print("Mulai remove number")
def remove_number(text):
    return  re.sub(r"\d+", "", text)

DATA['Hasil'] = DATA['Hasil'].apply(remove_number)

#remove punctuation
print("Mulai remove punctuation")
def remove_punctuation(text):
    return text.translate(str.maketrans(string.punctuation,"                                "))
# string.punctuation,"                                "
DATA['Hasil'] = DATA['Hasil'].apply(remove_punctuation)

#remove whitespace leading & trailing
print("Mulai remove whitespace leading & trailing")
def remove_whitespace_LT(text):
    return text.strip()

DATA['Hasil'] = DATA['Hasil'].apply(remove_whitespace_LT)

#remove multiple whitespace into single whitespace
print("Mulai remove multiple whitespace into single whitespace")
def remove_whitespace_multiple(text):
    return re.sub('\s+',' ',text)

DATA['Hasil'] = DATA['Hasil'].apply(remove_whitespace_multiple)

# remove single char
print("Mulai remove single char")
def remove_singl_char(text):
    return re.sub(r"\b[a-zA-Z]\b", "", text)

DATA['Hasil'] = DATA['Hasil'].apply(remove_singl_char)

# NLTK word tokenize 
print("Mulai word tokenize")
def word_tokenize_wrapper(text):
    return word_tokenize(text)

DATA['Hasil_tokens'] = DATA['Hasil'].apply(word_tokenize_wrapper)

print('Tokenizing Result : \n') 
# print(DATA['Hasil_tokens'].iloc[0])
print('\n\n\n')
def unique(document):
    unique_word = set()
    for i in document:
        unique_word = unique_word.union(i)
    return(unique_word)

uw = unique(DATA['Hasil_tokens'])
# print(uw)
# print(len(uw))

normalizad_word = pd.read_excel("Normalisasi.xlsx")

normalizad_word_dict = {}

for index, row in normalizad_word.iterrows():
    if row[0] not in normalizad_word_dict:
        normalizad_word_dict[row[0]] = row[1] 

print("Mulai normalized")
def normalized_term(document):
    return [normalizad_word_dict[term] if term in normalizad_word_dict else term for term in document]

DATA['Normal'] = DATA['Hasil_tokens'].apply(normalized_term)

# print(DATA['Normal'])
uw = unique(DATA['Normal'])
# print(uw)
# print(DATA['Normal'].iloc[0])

# difference = set(DATA['Normal'].iloc[0]).symmetric_difference(set(DATA['Hasil_tokens'].iloc[0]))
# list_difference = list(difference)
# print(list_difference)

# df = pd.read_csv("readytfidf.csv")

# for index, row in DATA.iterrows():
#     os.system('cls')
#     print(row['Normal'])
#     print(df['Normal'].iloc[index])
#     print()
#     input("lanjut : ")




#get indonesia stop word
list_stopwords = set(stopwords.words('indonesian'))
#remove stopwords pada list token
print("Mulai remove stopwords")
def stopword(text):
  tokens_without_stopword = [word for word in text if not word in list_stopwords]
  return tokens_without_stopword

DATA['Normal'] = DATA['Normal'].apply(stopword)

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stem
print("Mulai stem")
def stem(text):
  output   = [stemmer.stem(token) for token in text]
  return output

ready = pd.DataFrame()

DATA['Normal'] = DATA['Normal'].apply(stem)
print("Selesai Stem")
ready['Normal'] = DATA['Normal']
ready['Status'] = DATA['Status']
ready.to_csv('readytfidf.csv', index=False)