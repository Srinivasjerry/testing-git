vowels=['a','e','i','o','u']
word=input()
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print("the vowels are",word,'is at',len(found))