from Pre2 import Preprocessing
from tfidf import Pembobotan
from svm import algotirma
import time
start = time.time()
teks = "Membalas : Saham mana yg arb berhari2 IKAN mungkin wkwk"

Preprocessing(teks)
Pembobotan()
hasil = algotirma()

print(hasil)
end = time.time()
print(f"Runtime of the program is {end - start}")