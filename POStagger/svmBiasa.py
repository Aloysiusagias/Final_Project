from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# from sklearn.externals import joblib
from sklearn.pipeline import make_pipeline
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

svm = SVC(kernel='rbf')
cv = TfidfVectorizer(use_idf=True)

df = pd.read_csv('readytfidf3.csv')
df = df.sample(frac = 1)
# df['Status'] = df['Status'].replace(['Negatif', 'Positif', 'Netral'], ['0','1','2'])
y = df['Status']
X = df['Normal']
X = cv.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

svm = SVC(kernel='rbf', random_state=0)
svm.fit(X_train, y_train)
print('Akurasi sebelum pakai POS : ',svm.score(X_test, y_test))