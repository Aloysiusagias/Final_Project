import pandas as pd
import os

df = pd.read_csv('Scrap24April.csv', index_col=0)
# print(df.size)
# print(df.iloc[[2]]['Pesan'].values)
df["Status"] = "Belum"
for index, row in df.iterrows():
    Salah = True
    os.system('cls')
    print("Data :"+str(index))
    print(row['Pesan'])
    # df.loc[index, "Status"]="Positif"
    while Salah:
        a = input("Label : ")
        if (a=="h"):
            df.loc[index, "Status"]="Hapus"
            Salah = False
        elif (a=="p"):
            df.loc[index, "Status"]="Positif"
            Salah = False
        elif (a=="n"):
            df.loc[index, "Status"]="Negatif"
            Salah = False
        elif (a=="ne"):
            df.loc[index, "Status"]="Netral"
            Salah = False
        elif (a=="b"):
            df.loc[index, "Status"]="Bingung"
            Salah = False
        else :
            print("Inputan salah")
            Salah=True
df.to_csv("../Dataframe Siap/Dataset16.csv")