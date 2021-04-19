from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# from sklearn.externals import joblib
from Pre2 import Preprocessing
from sklearn.pipeline import make_pipeline
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
	# df= pd.read_csv("spam.csv", encoding="latin-1")
	# df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
	# # Features and Labels
	# df['label'] = df['class'].map({'ham': 0, 'spam': 1})
	# X = df['message']
	# y = df['label']
	
	# # Extract Feature With CountVectorizer
	# cv = CountVectorizer()
	# X = cv.fit_transform(X) # Fit the Data
	# from sklearn.model_selection import train_test_split
	# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
	# #Naive Bayes Classifier
	# from sklearn.naive_bayes import MultinomialNB

	# clf = MultinomialNB()
	# clf.fit(X_train,y_train)
	# clf.score(X_test,y_test)
	# #Alternative Usage of Saved Model
	# # joblib.dump(clf, 'NB_spam_model.pkl')
	# # NB_spam_model = open('NB_spam_model.pkl','rb')
	# # clf = joblib.load(NB_spam_model)

    # def prediksi(tekss):
    #     tekss = Preprocessing(tekss)
    #     print(tekss)
    #     vect = cv.transform([tekss])
    #     return svm.predict(vect)

    # teks = "Membalas : Saham mana yg arb berhari2 IKAN mungkin wkwk" #Negatif
    # teks = "Doid masih aman kalo belinya pas april 2020" #Positif
    teks = "Ati2 bank uda kena brp x suspend... Buangan nya banyak tuh barusan.jgn dikejar"

    svm = SVC(kernel='rbf')
    cv = TfidfVectorizer(use_idf=True)

    df = pd.read_csv('readytfidf.csv')
    df['Status'] = df['Status'].replace(['Negatif', 'Positif'], ['0','1'])
    y = df['Status']
    X = df['Normal']
    X = cv.fit_transform(X)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    svm.fit(X,y)
    # print("accuracy score: " + str(svm.score(X_test, y_test)))

    # for a in prediksi(teks):
    #     print("Prediksi : ",a)

    if request.method == 'POST':
        tekss = request.form['message']
        tekss = Preprocessing(tekss)
        print(tekss)
        vect = cv.transform([tekss])
        my_prediction = svm.predict(vect)
        my_prediction = int(my_prediction[0])
        print(my_prediction)
        # data = [message]
        # vect = cv.transform(data).toarray()
        # my_prediction = clf.predict(vect)
    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)