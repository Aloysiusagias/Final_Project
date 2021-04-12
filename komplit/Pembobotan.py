from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

text = {'Normal' : [['jelas', 'beda', 'ara', 'konsolidasi', 'tanpa']]}
df2 = pd.DataFrame(text, columns=['Normal'])
df = pd.read_csv('../readytfidf.csv')
print(df.iloc(0).values)
df3 = pd.DataFrame()
df3['Normal'] = df['Normal']
df = pd.concat([df2, df3])
# print(df)
# print(df['alur'])
# corpus = df['Normal']

# vectorizer = TfidfVectorizer(use_idf=True)
# tfidf = vectorizer.fit_transform(corpus)
# # print(tfidf[0])
# feature_names = vectorizer.get_feature_names()
# dense = tfidf.todense()
# denselist = dense.tolist()
# # df2 = pd.DataFrame(tfidf[0].T.todense(), index=vectorizer.get_feature_names(), columns=['TF-IDF'])
# # df2 = df2.sort_values('TF-IDF', ascending=False)
# df2 = pd.DataFrame(denselist, columns=feature_names)
# # df2['nilai'] = df['Status']
# print(df2)
# df2.to_csv('tfidf.csv')