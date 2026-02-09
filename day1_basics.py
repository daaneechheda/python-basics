#basics
print("Daanee")
print(100)
city = "mumbai"
print(city)
city = "delhi"
print(city)


#datatypes
age = 5
height = 5.5
name = "Daanee"
is_Learning = True

print(age)
print(height)
print(name)
print(is_Learning)

print(type(age))
print(type(height))
print(type(name))
print(type(is_Learning))


#conditions
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print ("You cannot vote")
print(type(age))




num = int(input("Enter a number: "))
if num>0:
    print("Positive")
elif num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Fail")
