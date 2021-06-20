def formatJam(teks):
    
    global sawaktu, tawaktu
    if(not "sawaktu" in globals()):
        sawaktu = ''
        tawaktu = 0
    # print('Jam nya adalah : '+teks)
    formm = teks.split()
    satuan = formm[1]
    jamm = formm[0]
    jamm = jamm.split(':')
    jam2 = jamm[0]
    menit = jamm[1]
    detik = jamm[2]
    formatt = jam2+menit+detik
    if(sawaktu!=satuan):
        sawaktu = satuan
        tawaktu +=1
    formatt = str(tawaktu) + formatt
    return int(formatt)

jam = formatJam('12:34:56 AM')
print(jam)
jam = formatJam('12:11:33 AM')
print(jam)
jam = formatJam('12:34:56 PM')
print(jam)
jam = formatJam('12:32:12 AM')
print(jam)