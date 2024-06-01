#AddData.py
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facial-recognition-atten-53da8-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "B045":
        {
            "name": "Margot Robbie",
            "major": "Acting",
            "starting_year": 2020,
            "total_attendance": 76,
            "grade": "A+",
            "year": 3,
            "last_attendance_time": "2023-10-15 14:16:15"
        },
    "B046":
        {
            "name": "Cristiano Ronaldo",
            "major": "Football",
            "starting_year": 2003,
            "total_attendance": 95,
            "grade": "A",
            "year": 20,
            "last_attendance_time": "2023-10-15 14:16:15"
        },
    "B048":
        {
            "name": "Ryan Gosling (Me)",
            "major": "Acting",
            "starting_year": 2019,
            "total_attendance": 84,
            "grade": "A+",
            "year": 4,
            "last_attendance_time": "2023-10-15 14:16:15"
        }

}

for key,value in data.items():
    ref.child(key).set(value)