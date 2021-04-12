import pandas as pd

# df1 = pd.read_csv("Dataframe Siap/Dataset4.csv")
# df2 = pd.read_csv("Dataframe Siap/Dataset5.csv")
# df3 = pd.read_csv("Dataframe Siap/Dataset6.csv")

# df1P = df1[df1["Status"]=="Positif"]
# df1N = df1[df1["Status"]=="Negatif"]
# df1 =[df1P,df1N]
# df1 = pd.concat(df1)

# df2P = df2[df2["Status"]=="Positif"]
# df2N = df2[df2["Status"]=="Negatif"]
# df2 =[df2P,df2N]
# df2 = pd.concat(df2)

# df3P = df3[df3["Status"]=="Positif"]
# df3N = df3[df3["Status"]=="Negatif"]
# df3 =[df3P,df3N]
# df3 = pd.concat(df3)

# result = pd.concat([df1, df2, df3])

# print(result)
# print(len(result[result["Status"]=="Positif"]))
# print(len(result[result["Status"]=="Negatif"]))

# result.to_csv("Dataframe Siap/Dataframe1.csv")


df1 = pd.read_csv("Dataframe Siap/Dataframe.csv")
df2 = pd.read_csv("Dataframe Siap/Dataframe1.csv")

result = pd.concat([df1, df2])

print(result)
print(len(result[result["Status"]=="Positif"]))
print(len(result[result["Status"]=="Negatif"]))

result.to_csv("Dataframe Siap/Dataframe ready.csv")