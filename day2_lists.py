#Basic List
marks = [70, 85, 90, 60, 75]
print(marks[0])
print(marks[-1])
print(len(marks))

#Update List
marks[3] = 65
print(marks)

#Loop Through List
for m in marks:
    print(m)

#Count Even Numbers
count = 0
nums = [10, 21, 4, 45, 66, 93]
for i in nums:
    if i%2 == 0:
        count = count + 1
print(count)

#Find Maximum (Manual)
nums1 = [10, 21, 4, 45, 66, 93]
max_val = nums1[0]
for i in nums1:
    if i>max_val:
        max_val = i
print(max_val)

#Find Minimum (Manual)
min_val = nums1[0]
for i in nums1:
    if i<min_val:
        min_val = i
print(min_val)

password = ""

while password != "python123":
	password = input("enter password: ")

print("Access granted")