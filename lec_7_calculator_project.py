#automatic Arthmetic operator (Example)
bottels=8
bear=45
cream=8
mobile=8
cup=7
brush=7
dairy=8
print(f"addition:{bottels+bear+cream+mobile+cup+brush+dairy}")
print(f"subtraction:{bottels-bear-cream-mobile-cup-brush-dairy}")
print(f"multiplication:{bottels*bear*cream*mobile*cup*brush*dairy}")
print(f"division:{bottels/bear/cream/mobile/cup/brush/dairy}")



shirt=22
pant=23
trouser=2
jeans=22
mobile=2
print(f"addition:{shirt+pant+trouser+jeans+mobile}")





































2#Basic calculator with operator choice

a = input("enter first number: ")
b = input("Enter second number: ")
op = input("Enter operator (+, -, *, /): ")


a=int(a)
b=int(b)

if op == "+":
    print("Result:", a + b)
elif op == "-":
 print("Result:", a - b)
elif op== "*":
 print("Result:", a * b)
elif op == "/":
  ("Result:", a / b)
else:
  print("Invalid operator")

# Simple Arithmetic Operations - Step by Step
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#Advanced Arithmetic Operations with Exponentiation and Floor Division

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Addition
print(f"Addition: {a + b}")

#Subtraction
print(f"Subtraction: {a - b}")

# Multiplication
print(f"Multiplication: {a * b}")

# # Division
print(f"Division: {a / b}")

# # Exponentiation (Power)
print(f"Exponentiation (a^b): {a ** b}")

# # Floor Division (Quotient without remainder)
print(f"Floor Division: {a // b}")

# # Modulus (Remainder)
print(f"Remainder: {a % b}")



a=int(input("enter first number "))
b=int(input("enter second number"))

print(f"addition:{a+b}")
print(f"subtraction:{a-b}")
print(f"multiplication:{a*b}")
print(f"division:{a/b}")

a=9
b=9

print(f"addition:,{a+b}")
print(f"subtraction:{a-b}")
print(f"multiplication:{a*b}")
print(f"division:{a/b}")



a=int(input("enter first number"))
b=int(input("enter second number"))
op=(input("+,-,*,/"))

a=int(a)
b=int(b)

if op=="+":
  print(f"result:{a+b}")
elif op=="-":
  print(f"result:{a-b}")
elif op=="*":
  print(f"result:{a*b}")
elif op=="/":
  print("result:{a/b}")
else:
  print("invalid opertor")

number1=int(input("enter the value of first no.="))
number2=int(input("enter second value of second no.="))

add=number1+number2

print("the sub of ",number1,"and",number2,"is",add)
sub=number1-number2
print("the substraction of",number1,"and",number2,"is",sub)
div= number1/number2
print("the division of",number1,"and",number2,"is",div)
div=number1/number2
print("the division of",number1,"and",number2,"is",div)
flr=number1//number2
print("the floor division of",number1,"and",number2,"is",flr)
exp=number1**number2
