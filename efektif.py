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
from sklearn.model_selection import GridSearchCV

svm = SVC(kernel='rbf')
cv = TfidfVectorizer(use_idf=True)

df = pd.read_csv('Telegram API/readytfidf3.csv')
df = df.sample(frac = 1)
df['Status'] = df['Status'].replace(['Negatif', 'Positif', 'Netral'], ['0','1','2'])
y = df['Status']
X = df['Normal']
X = cv.fit_transform(X)

params_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100],
          'gamma': [0.0001, 0.001, 0.01, 0.1, 1, 10, 100],
          'kernel':['linear','rbf'] }


for i in range(40):
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=27)
    # svm.fit(X_train,y_train)

    clf = GridSearchCV(SVC(class_weight='balanced', random_state=i), params_grid)
    grid_clf = clf.fit(X, y)
    print('random_state =',i)
    print(grid_clf.best_params_)
    print(grid_clf.best_score_)
    print('-'*30)