import pandas as pd

df = pd.read_csv('Dataframe Ready.csv')
df1 = pd.read_csv('buatan.csv',index_col=0)

df = df.append(df1)
print(df[df['Status']=='Netral'])

df.to_csv('Data baru.csv')