import pandas as pd
import time

df = pd.read_csv('Siap.csv')
# print(df)
user =df['User'].unique() 
hit = dict((el,0) for el in user)
miss = dict((el,0) for el in user)
print(hit)
print(len(user))