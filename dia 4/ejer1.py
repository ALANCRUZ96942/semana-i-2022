'''
Python Firebase Course for
Beginners
https://codeloop.org/python-firebase-course-for-beginners/
'''

import pyrebase
from getpass import getpass


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
auth = firebase.auth()
#get the valid email and password from the user
email = input("Please Enter Your Email : ")
password = getpass('Please Enter Your Password : ')
#and authenticate the user
user = auth.create_user_with_email_and_password(email, password)
print("User Created Successfully")
#For accesing the firebase after the creation of user by email
try:
    signin = auth.sign_in_with_email_and_password(email, password)
    print("Sign In Was Successfull")
except:
    print("Invalid user or password")
#Verification of user
auth.send_email_verification(signin['idToken'])
print("Email Verification Has Been Sent")
#Reset the password
auth.send_password_reset_email(email)
print("We have sent an email, check your inbox ")
