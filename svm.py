import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv('tfidf.csv', index_col=0)
# print(df['one'].unique())
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
svm.fit(X_train, y_train)
print(svm.score(X_test, y_test))
# a = svm.predict(X_test)
# print(X_test)
# print(len(a))
# print(a)
# print(accuracy_score(y_test, a))

# print(y_test)
# for x in range(20):
#     print(X_test[x])
#     print(a[x])