import mysql.connector

def insertt(data):
  user = data['user']
  pesan = data['pesan']
  prediksi = data['prediksi']
  balas_user = data['balas_user']
  balas_pesan = data['balas_pesan']
  grup = data['grup']

  grup = grup.replace(' ', '_')
  grup = grup.lower()

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tele"
  )

  mycursor = mydb.cursor()
  cek_grup(mycursor, grup)

  sql = "INSERT INTO "+grup+" (user, pesan, prediksi, balas_user, balas_pesan) VALUES (%s, %s,%s, %s,%s)"
  val = (user, pesan, prediksi, balas_user, balas_pesan)
  mycursor.execute(sql, val)

  mydb.commit()


def cek_grup(mycursor, grup):
    sql = "SHOW TABLES"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    ada = False
    print(grup)
    for i in myresult:
        print(i[0])
        if(i[0] == grup):
            ada = True
    
    if (not ada):
        sql = "CREATE TABLE "+grup+" ( ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, user VARCHAR(20), pesan VARCHAR(1000), prediksi VARCHAR(10), balas_user VARCHAR(20), balas_pesan VARCHAR(1000))"
        mycursor.execute(sql)