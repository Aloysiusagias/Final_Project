import pandas as pd
import time
import pandas_datareader.data as web
import datetime as dt

# df = pd.read_csv('Siap.csv')
# # print(df)
# user =df['User'].unique() 
# hit = dict((el,0) for el in user)
# miss = dict((el,0) for el in user)
# print(hit)
# print(len(user))
b = "TLKM.JK"
g = dt.datetime(2021,4,7)
start = g - dt.timedelta(days=1)
finish = g + dt.timedelta(days=1)
source = 'yahoo'

df = web.DataReader('TLKM.JK', source, start, finish)
print(df)