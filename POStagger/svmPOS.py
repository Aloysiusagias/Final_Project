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
df_new = df_new.sample(frac = 1)
# print(df_new['Status'])
X = df_new.drop(['Status'], axis=1)
y = df_new['Status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

svm = SVC(kernel='rbf', random_state=0)
svm.fit(X_train, y_train)
print('Akurasi setelah pakai POS : ',svm.score(X_test, y_test))
plot_confusion_matrix(svm, X_test, y_test)














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
