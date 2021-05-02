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
from Pre2 import Preprocessing

def svm(teks):
    print('Teks yang masuk adalah : ',teks)
    svm = SVC(kernel='rbf')
    cv = TfidfVectorizer(use_idf=True)

    df = pd.read_csv('readytfidf3.csv')
    df = df.sample(frac = 1)
    df['Status'] = df['Status'].replace(['Negatif', 'Positif'], ['0','1'])
    y = df['Status']
    X = df['Normal']
    X = cv.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    svm.fit(X_train,y_train)
    tekss = Preprocessing(teks)
    # print(tekss)
    vect = cv.transform([tekss])
    my_prediction = svm.predict(vect)
    my_prediction = int(my_prediction[0])
    if (my_prediction==0):
        my_prediction='Negatif'
    elif (my_prediction==1):
        my_prediction='Positif'
    else :
        my_prediction='Netral'
    # print("accuracy score: " + str(svm.score(X_test, y_test)))
    # print(my_prediction)
    return my_prediction
