# Simple user credential
user = 'admin'
password = 'admin@123'

user1 = input("Enter your user name  : ")
passw = input("Enter your password to login  : ")

if(user1 == user and passw == password):
  print("login successful ")
  print("welcome ", user1)
elif(user1 == user):
  print("user password is incorrect ")
elif(passw == password):
  print("Invalid user name")
else:
  print("Invalid user name and password")