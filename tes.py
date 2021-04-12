# import string
# import pandas as pd
# import yfinance as yf
import numpy as np
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
from sklearn.metrics import confusion_matrix

# df = pd.read_csv("Dataframe Siap/Dataframe.csv")
# print(len(df[df["Status"]=="Positif"]))
# print(len(df[df["Status"]=="Negatif"]))

# print(type(string.punctuation))
# print(string.punctuation)

start = dt.datetime(2021,4,7)
finish = dt.datetime.today()
source = 'yahoo'

df = web.DataReader('TLKM.JK', source, start, finish)
print(df.head())