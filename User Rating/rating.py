import numpy as np
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
from sklearn.metrics import confusion_matrix
import calendar
from time import strptime

df = pd.read_csv('Siap.csv')
user = df['User'].unique() 
hit = dict((el,0) for el in user)
miss = dict((el,0) for el in user)
c = 299
for index, row in df.iterrows():
    a = row['Saham']
    a = a.split(',')
    status = row['Status']
    pesan = row['Pesan']
    datee = row['Tanggal']
    datee = datee.split(" ")
    userr = row['User']

    monthWord = datee[1]
    newWord = monthWord [0].upper() + monthWord [1:3].lower()
    month = int(strptime(newWord,'%b').tm_mon)
    date = int(datee[2])
    year = int(datee[3])

    dateAfter = int(date)+1
    date = date-1

    start = dt.datetime(year,month,date)
    finish = dt.datetime(year,month,dateAfter)
    source = 'yahoo'

    for d in a:
        print(d)
        b = d+'.JK'
        bisa = False
        while not bisa:
            try :
                df1 = web.DataReader(b, source, start, finish)
                bisa = True
            except :
                continue
        print (df1)
        if (len(df1) > 1):
            openn = df1.iloc[-2]['Open']
            close = df1.iloc[-1]['Close']
            print(df1)
            if(close > openn):
                temp = "Positif"
            else :
                temp = 'Negatif'

            if (temp==status):
                print("Hit")
                hit[userr] += 1
            else :
                print("Miss")
                miss[userr] += 1

            print("Reality : ",temp)
            print("Status : ",status)
            print(pesan)
        else : 
            print('Skip')
    print('='*50)

print('\n\n\n')
for (k,v), (k2,v2) in zip(hit.items(), miss.items()):
    if (k==k2):
        print(k)
        print("Hit : ", v)
        print("Miss : ", v2)
        rate = int(v)/(int(v) + int(v2))
        print("User Rating : ",str(rate))