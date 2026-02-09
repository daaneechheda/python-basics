#Count Vowels
word = input("Enter a word: ")
word = word.lower()
count = 0
for i in word:
    if i == "a":
        count+=1
    elif i == "e":
        count+=1
    elif i == "i":
        count+=1
    elif i == "o":
        count+=1
    elif i == "u":
        count+=1
print(count)
    
#Reverse a String (MANUAL)
words = ""
n = -1
for i in range(len(word)):
    words =words + word[n]
    n = n-1
print(words)

#Palindrome Check
if word == words:
    print("Palindrome")
else:
    print("Not Palindrome")