import pandas as pd
import json

df = pd.read_csv('Rating.csv')

a = {'Rating' : {

}}
for idx, rows in df.iterrows():
    a['Rating'][rows['User']] = {
        'Hit' : rows['Hit'],
        'Miss' : rows['Miss'],
        'Rate' : rows['Rate'],
    }
print(a)

with open("sample.json", "w") as outfile: 
    json.dump(a, outfile)