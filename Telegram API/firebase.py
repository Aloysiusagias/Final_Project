import pyrebase

def insertt(data):
    firebaseConfig = {
        "apiKey": "AIzaSyBO9fmyGtUOGCnG_4CcXXwCMGlUGSIRi38",
        "authDomain": "finalproject-af65a.firebaseapp.com",
        "databaseURL": "https://finalproject-af65a-default-rtdb.asia-southeast1.firebasedatabase.app",
        "projectId": "finalproject-af65a",
        "storageBucket": "finalproject-af65a.appspot.com",
        "messagingSenderId": "120718877342",
        "appId": "1:120718877342:web:d6e808dbcf42ec5035518f",
        "measurementId": "G-VWZDM26D4Z"
    };

    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()

    db.child('grup/'+data['grup']).push(data)
