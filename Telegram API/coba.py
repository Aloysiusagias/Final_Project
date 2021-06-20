import mysql.connector

def cek_grup():
    grup = 'Percobaan_TA'
    ada = False

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tele"
    )

    mycursor = mydb.cursor()
    sql = "SHOW TABLES"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for i in myresult:
        print(i[0])
        if(i == grup):
            ada = True
    
    if (not ada):
        sql = "CREATE TABLE "+grup+" ( ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, user VARCHAR(20), pesan VARCHAR(1000), prediksi VARCHAR(10), balas_user VARCHAR(20), balas_pesan VARCHAR(1000))"
        mycursor.execute(sql)

cek_grup()