import pandas as pd
from nltk.corpus import stopwords

df = pd.read_csv("Dataframe3.csv")
df2 = pd.DataFrame()
df2[["Pesan", "Status"]] = df[["Pesan", "Status"]]
df2.to_csv("Dataframe Ready.csv", index=False)

# df = pd.read_csv("Dataframe2.csv")
# print(len(df[df["Status"]=="Positif"]))
# dt = [{
#     "Pesan" :"Pyfa mulai naik di penutupan sesi",
#     "Status" : "Belum"
# }]
# smt = pd.DataFrame(dt)
# smt = pd.concat([smt, df], ignore_index=True)