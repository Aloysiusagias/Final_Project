import pandas as pd
import time
import pandas_datareader.data as web
import datetime as dt

# # df = pd.read_csv('Siap.csv')
# # # print(df)
# # user =df['User'].unique() 
# # hit = dict((el,0) for el in user)
# # miss = dict((el,0) for el in user)
# # print(hit)
# # print(len(user))
# # b = "TLKM.JK"
# # g = dt.datetime(2021,4,7)
# # start = g - dt.timedelta(days=1)
# # finish = g + dt.timedelta(days=1)
# # source = 'yahoo'

# # df = web.DataReader('TLKM.JK', source, start, finish)
# # print(df)
# df = pd.read_csv('Siap.csv')
# satu = df.iloc[0]['Jam']
# formm = satu.split()
# satuan = formm[1]
# jamm = formm[0]
# jamm = jamm.split(':')
# jam = jamm[0]
# menit = jamm[1]
# detik = jamm[2]
# # print(jam, menit, detik, satuan)
# if(int(jam)<12):
#     print("pagi")


df = pd.read_csv('Rating.csv')
# print(df)

user = 'Aloysious Agias'
exist = user in df.User.values

df1 = df[df['User']==user]
# hit = df1.iloc[0]['Hit']
# miss = df1.iloc[0]['Miss']
# rate = df1.iloc[0]['Rate']
print(exist)