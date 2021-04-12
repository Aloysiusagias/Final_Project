from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def Pembobotan() :
    print("Pembobotan Mulai")
    df = pd.read_csv('readytfidf.csv')
    # print(df['alur'])
    corpus = df['Normal']

    vectorizer = TfidfVectorizer(use_idf=True)
    tfidf = vectorizer.fit_transform(corpus)
    # print(tfidf[0])
    feature_names = vectorizer.get_feature_names()
    dense = tfidf.todense()
    denselist = dense.tolist()
    # df2 = pd.DataFrame(tfidf[0].T.todense(), index=vectorizer.get_feature_names(), columns=['TF-IDF'])
    # df2 = df2.sort_values('TF-IDF', ascending=False)
    df2 = pd.DataFrame(denselist, columns=feature_names)
    df2['nilai'] = df['Status']
    # return df2
    # print(df2)
    df2.to_csv('tfidf.csv')