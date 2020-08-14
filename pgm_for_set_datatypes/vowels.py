w=input("Enter the word:")
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)
print("The vowels present in",w,"is",d)
