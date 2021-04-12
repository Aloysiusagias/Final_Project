from Pre2 import Preprocessing
from tfidf import Pembobotan
from svm import algotirma
import time
start = time.time()
teks = "Serok wsbp lumayan"

Preprocessing(teks)
Pembobotan()
hasil = algotirma()

print(hasil)
end = time.time()
print(f"Runtime of the program is {end - start}")