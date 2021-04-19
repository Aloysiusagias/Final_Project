from Pre2 import Preprocessing
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

def prediksi(tekss):
    tekss = Preprocessing(tekss)
    print(tekss)
    vect = cv.transform([tekss])
    return svm.predict(vect)

# teks = "Membalas : Saham mana yg arb berhari2 IKAN mungkin wkwk" #Negatif
# teks = "Doid masih aman kalo belinya pas april 2020" #Positif
teks = "Ati2 bank uda kena brp x suspend... Buangan nya banyak tuh barusan.jgn dikejar"

svm = SVC(kernel='rbf')
cv = TfidfVectorizer(use_idf=True)

df = pd.read_csv('readytfidf.csv')
y = df['Status']
X = df['Normal']
X = cv.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
svm.fit(X_train,y_train)
print("accuracy score: " + str(svm.score(X_test, y_test)))

for a in prediksi(teks):
    print("Prediksi : ",a)