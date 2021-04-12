import pandas as pd

df1 = pd.read_csv('SahamSudah.csv')
df2 = pd.read_csv('../Dataframe Siap/Dataset2sudah.csv')
df3 = pd.read_csv('../Dataframe Siap/Dataset3sudah.csv')
df4 = pd.read_csv('../Dataframe Siap/Dataset4sudah.csv')
df5 = pd.read_csv('../Dataframe Siap/Dataset5sudah.csv')
df6 = pd.read_csv('../Dataframe Siap/Dataset6sudah.csv')


df1P = df1[df1["Status"]=="Positif"]
df1N = df1[df1["Status"]=="Negatif"]
df1 =[df1P,df1N]
df1 = pd.concat(df1)

# df2P = df2[df2["Status"]=="Positif"]
# df2N = df2[df2["Status"]=="Negatif"]
# df2 =[df2P,df2N]
# df2 = pd.concat(df2)

# df3P = df3[df3["Status"]=="Positif"]
# df3N = df3[df3["Status"]=="Negatif"]
# df3 =[df3P,df3N]
# df3 = pd.concat(df3)

df4P = df4[df4["Status"]=="Positif"]
df4N = df4[df4["Status"]=="Negatif"]
df4 =[df4P,df4N]
df4 = pd.concat(df4)

df5P = df5[df5["Status"]=="Positif"]
df5N = df5[df5["Status"]=="Negatif"]
df5 =[df5P,df5N]
df5 = pd.concat(df5)

df6P = df6[df6["Status"]=="Positif"]
df6N = df6[df6["Status"]=="Negatif"]
df6 =[df6P,df6N]
df6 = pd.concat(df6)

result = pd.concat([df1, df4, df5, df6])
result = result[['User', 'Pesan','Saham', 'Jam', 'Tanggal', 'Status']]
result.to_csv('Siap.csv', index=False)
print(result)