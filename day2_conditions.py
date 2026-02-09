#number analyzer
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#Grading system
marks = int(input("Enter marks: "))
if marks>=90 and marks<=100:
    print("A")
elif marks>=75 and marks<=89:
    print("B")
elif marks>=50 and marks<=74:
    print("C")
else:
    print("Fail")

#Login logic
user = input("Enter username: ")
password = input("Enter password: ")

if user == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid creds")
