#Loops
#for loop
square = 0
for i in range(1,6):
    square = i * i
    print(square)

even = 0
for e in range(1,11):
    if e%2 == 0:
        print(e)


total = 0
for i in range(1,11):
    total = total+i
print(total)

num = 7
for c in range(1,11):
    mul = num * c
    print(num, "x", c ,"=", mul)

for t in range(5):
    print("*****")


#while loop
num = 1
while num<11:
    print(num)
    num = num + 1

num = 0
while num<20:
    num = num + 1
    if num%2 == 0:
        
        continue
    print(num)


while True:
    numb = int(input("Enter a number: "))
    print(numb)
    if numb == 0:
        break

nnum = 0
sum  = 0
while nnum <50:
    nnum += 1
    sum = sum + nnum
print(sum)
