s="Python is easy"
n=len(s)
i=0
print("Forward direction")
while i<n:
    print(s[i],end='')
    i+=1
print("Backward direction")
i=-1
while i>=-n:
    print(s[i],end='')
    i=i-1
