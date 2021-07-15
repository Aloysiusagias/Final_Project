import pandas as pd
from nltk.tokenize import word_tokenize 

df = pd.read_csv('readytfidf3.csv')

def word_tokenize_wrapper(text):
    return word_tokenize(text)

df['token'] = df['Normal'].apply(word_tokenize_wrapper)

df.to_csv('Data2.csv')