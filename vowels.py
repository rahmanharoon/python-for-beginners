vowels=['a','e','i','o','u']
word=input("Enter the word:")
found=[]
for letter in word:
    if letter in vowels:
        found.append(letter)
print(found)
print("The no of vowels present in",word,"is",len(found))
        
