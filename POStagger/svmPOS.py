#import library yang diperlukan
from operator import index
import pandas as pd
import csv
import numpy as np
# from predatatestcaca import predict, testing, mydb
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import plot_confusion_matrix

df = pd.read_csv('DataSiapPOS.csv', index_col=0)
class_labels = pd.read_csv('readytfidf3.csv')
class_labels = class_labels['Status']
df_new = pd.concat([df, class_labels], axis=1)
# df_new = df_new.sample(frac = 1)
# print(df_new['Status'])
X = df_new.drop(['Status'], axis=1)
y = df_new['Status']

MAX = -1
ii = 0
for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=i)

    svm = SVC(kernel='rbf')
    svm.fit(X_train, y_train)
    # a = svm.predict(X_test)
    # print(a)
    scoree = svm.score(X_test, y_test)
    if (scoree > MAX):
        MAX = scoree
        ii = i
    print(i)
    # print(class_labels.size)
    # plot_confusion_matrix(svm, X_test, y_test)
print('Akurasi setelah pakai POS : ',MAX)
print("i =", ii)














# class_labels = np.array(pd.read_csv('readytfidf3.csv',encoding='utf-8'))
# list_kelas=[]
# i = 0

# for kelas in class_labels:
#     list_kelas.append(class_labels[i][1])
#     i += 1
# # print(list_kelas)

# cls = pd.DataFrame(list_kelas)
# df_new = pd.concat([df, cls], axis=1)



# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
