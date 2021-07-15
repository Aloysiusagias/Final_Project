import pandas as pd

a = ""
b = ''
df = pd.DataFrame(columns = ['Pesan', 'Status'])
while a != "y":
    b = input("Masukkan label : ")
    while a!="sudah":
        a = input("Masukkan kalimat : ")
        # df2 = pd.DataFrame([a,b])
        if(a!="sudah"):
            df = df.append({'Pesan' : a, 'Status' : b}, 
                    ignore_index = True)
    a = input("Selesai?")
df.to_csv("Buatan hold2.csv")