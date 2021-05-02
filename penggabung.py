import pandas as pd

df1 = pd.read_csv("Dataframe Siap/DatasetSudah.csv")
df2 = pd.read_csv("Dataframe Siap/Dataset2Sudah.csv")
df3 = pd.read_csv("Dataframe Siap/Dataset3Sudah.csv")
df4 = pd.read_csv("Dataframe Siap/Dataset4Sudah.csv")
df5 = pd.read_csv("Dataframe Siap/Dataset5Sudah.csv")
df6 = pd.read_csv("Dataframe Siap/Dataset6Sudah.csv")
df7 = pd.read_csv("Dataframe Siap/Dataset7.csv")
df8 = pd.read_csv("Dataframe Siap/Dataset8.csv")
df9 = pd.read_csv("Dataframe Siap/Dataset9.csv")
df10 = pd.read_csv("Dataframe Siap/Dataset10.csv")
df11 = pd.read_csv("Dataframe Siap/Dataset11.csv")
df12 = pd.read_csv("Dataframe Siap/Dataset12.csv")

df1P = df1[df1["Status"]=="Positif"]
df1N = df1[df1["Status"]=="Negatif"]
df1NE = df1[df1["Status"]=="Netral"]
df1b =[df1P,df1N, df1NE]
df1b = pd.concat(df1b)

df2P = df2[df2["Status"]=="Positif"]
df2N = df2[df2["Status"]=="Negatif"]
df2NE = df2[df2["Status"]=="Netral"]
df2b =[df2P,df2N, df2NE]
df2b = pd.concat(df2b)

df3P = df3[df3["Status"]=="Positif"]
df3N = df3[df3["Status"]=="Negatif"]
df3NE = df3[df3["Status"]=="Netral"]
df3b =[df3P,df3N, df3NE]
df3b = pd.concat(df3b)

df4P = df4[df4["Status"]=="Positif"]
df4N = df4[df4["Status"]=="Negatif"]
df4NE = df4[df4["Status"]=="Netral"]
df4b =[df4P,df4N, df4NE]
df4b = pd.concat(df4b)

df5P = df5[df5["Status"]=="Positif"]
df5N = df5[df5["Status"]=="Negatif"]
df5NE = df5[df5["Status"]=="Netral"]
df5b =[df5P,df5N, df5NE]
df5b = pd.concat(df5b)

df6P = df6[df6["Status"]=="Positif"]
df6N = df6[df6["Status"]=="Negatif"]
df6NE = df6[df6["Status"]=="Netral"]
df6b =[df6P,df6N, df6NE]
df6b = pd.concat(df6b)

df7P = df7[df7["Status"]=="Positif"]
df7N = df7[df7["Status"]=="Negatif"]
df7NE = df7[df7["Status"]=="Netral"]
df7b =[df7P,df7N, df7NE]
df7b = pd.concat(df7b)

df9P = df9[df9["Status"]=="Positif"]
df9N = df9[df9["Status"]=="Negatif"]
df9NE = df9[df9["Status"]=="Netral"]
df9b =[df9P,df9N, df9NE]
df9b = pd.concat(df9b)

df8P = df8[df8["Status"]=="Positif"]
df8N = df8[df8["Status"]=="Negatif"]
df8NE = df8[df8["Status"]=="Netral"]
df8b =[df8P,df8N, df8NE]
df8b = pd.concat(df8b)

df10P = df10[df10["Status"]=="Positif"]
df10N = df10[df10["Status"]=="Negatif"]
df10NE = df10[df10["Status"]=="Netral"]
df10b =[df10P,df10N, df10NE]
df10b = pd.concat(df10b)

df11P = df11[df11["Status"]=="Positif"]
df11N = df11[df11["Status"]=="Negatif"]
df11NE = df11[df11["Status"]=="Netral"]
df11b =[df11P,df11N, df11NE]
df11b = pd.concat(df11b)

df12P = df12[df12["Status"]=="Positif"]
df12N = df12[df12["Status"]=="Negatif"]
df12NE = df12[df12["Status"]=="Netral"]
df12b =[df12P,df12N, df12NE]
df12b = pd.concat(df12b)

print(df12b)

# df3P = df3[df3["Status"]=="Positif"]
# df3N = df3[df3["Status"]=="Negatif"]
# df3 =[df3P,df3N]
# df3 = pd.concat(df3)

# result = pd.concat([df1, df2, df3])

# print(result)
# print(len(result[result["Status"]=="Positif"]))
# print(len(result[result["Status"]=="Negatif"]))

# result.to_csv("Dataframe Siap/Dataframe1.csv")


# df1 = pd.read_csv("Dataframe Siap/Dataframe.csv")
# df2 = pd.read_csv("Dataframe Siap/Dataframe1.csv")

result = pd.concat([df1b, df2b, df3b, df4b, df5b, df6b, df7b, df8b, df9b, df10b, df11b, df12b])
result2 = result[['User','Pesan','Jam','Tanggal','Status']]
# print(df1b[['Pesan', 'Status']])
result2.reset_index(inplace=True)
result2.drop('index', axis=1, inplace=True)
print(result2)
print(len(result2[result2["Status"]=="Positif"]))
print(len(result2[result2["Status"]=="Negatif"]))
print(len(result2[result2["Status"]=="Netral"]))

result2.to_csv("Dataframe Siap/Dataframe baru rating.csv", index=False)