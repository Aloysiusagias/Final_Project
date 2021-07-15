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

# import mysql.connector

# def cek_grup():
#     grup = 'Percobaan_TA'
#     ada = False

#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="tele"
#     )

#     mycursor = mydb.cursor()
#     sql = "SHOW TABLES"
#     mycursor.execute(sql)
#     myresult = mycursor.fetchall()

#     for i in myresult:
#         print(i[0])
#         if(i == grup):
#             ada = True
    
#     if (not ada):
#         sql = "CREATE TABLE "+grup+" ( ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, user VARCHAR(20), pesan VARCHAR(1000), prediksi VARCHAR(10), balas_user VARCHAR(20), balas_pesan VARCHAR(1000))"
#         mycursor.execute(sql)

# cek_grup()
# svm = SVC(kernel='rbf')
# cv = TfidfVectorizer(use_idf=True)

# df = pd.read_csv('NEWDATA.csv')
# df.dropna(subset=["Normal"],inplace=True)
# df = df.sample(frac = 1)
# y = df['Status']
# X = df['Normal']
# X = cv.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
# svm.fit(X_train,y_train)
# print(svm.score(X_test,y_test))
def ambil_rating(user):
    rate = pd.read_csv('Rating.csv',index_col=0)
    a = rate[rate['User']==user]
    if(not a.empty):
        print(a)
        hit = a.iloc[0][1]
        miss = a.iloc[0][2]
        rating = a.iloc[0][3]
    else :
        hit = "No record"
        miss = "No record"
        rating = "No record"
    return {
        "hit" : hit,
        "miss" : miss,
        "rating" : rating
    }
b = ambil_rating("ryanless")
print(b["hit"], b["miss"], b["rating"])