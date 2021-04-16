import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def algotirma():
    print("Algoritma Mulai")
    df = pd.read_csv('tfidf.csv', index_col=0)
    test = pd.DataFrame()
    test = df.iloc[[0]]
    test = test.drop('nilai',axis=1)
    df.drop(0, inplace = True)
    df['nilai'] = df['nilai'].replace(['Negatif', 'Positif'], ['0','1'])
    # print(df)
    y = df['nilai']
    X = df.drop('nilai',axis=1)
    # print('=====================')
    # print(y)
    # print(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
    # print(X_test)
    svm = SVC(kernel='rbf')
    svm.fit(X, y)
    print(svm.score(X_test, y_test))
    if (svm.predict(test) == '1'):
        return("Positif")
    elif (svm.predict(test) == '0'):
        return("Negatif")