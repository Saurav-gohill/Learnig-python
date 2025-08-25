# A simple Calculator
a= int(input ("first number "))
c = input("you operation what you want : +, -, *, /, //, %, ** : ")
b = int(input ("second number "))

if c == '+':
  print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
  print(a*b)
elif c == '/':
  print(a/b)
elif c == '//':
  print(a//b)
elif c == '%':
  print(a%b)
elif c == '**':
  print(a**b)
else:
  print("You enter wrong input")