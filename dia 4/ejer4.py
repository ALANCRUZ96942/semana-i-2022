'''
Python Firebase Course for
Beginners
https://codeloop.org/python-firebase-course-for-beginners/
'''
import pyrebase

config = {
  "apiKey": "AIzaSyDAevrT5wmuxqptMnlTghUnvpZPV0pfTa4",
  "authDomain": "esp-32-semana-i-523bd.firebaseapp.com",
  "databaseURL": "https://esp-32-semana-i-523bd-default-rtdb.firebaseio.com",
  "projectId": "esp-32-semana-i-523bd",
  "storageBucket": "esp-32-semana-i-523bd.appspot.com",
  "messagingSenderId": "506603944398",
  "appId": "1:506603944398:web:06afeee9cf250b65fa539f"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()
#create your onKey, for label elements
#update elements
db.child("users").child("Gatitos").update({"name":"Juan Camanaey"})
print("Data updated successfully ")

db.child("users").child("-NFOzT4VR1FlqTd1OD9a").update({"name":"Alan Cruz G"})#-LzqIcMVMPaQKVLLjK5d is an onKey designated by omision in Firebase
print("Data updated successfully ")

#accesing database in firebase
db = firebase.database()
#reading some atributes of the onKey elements
all_users = db.child("users").get()

for users in all_users.each():
    print(users.val())
    print(users.key())
