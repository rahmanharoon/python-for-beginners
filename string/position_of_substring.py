s=input("Enter main string:")
sub=input("Enter sub string:")
flag=False
pos=-1
n=len(s)
while True:
    pos=s.find(sub,pos+1,n)
    if pos==-1:
        break
    print("Found at position",pos)
if flag==False:
    print("Not found")


b="ababbbaaba"
print(s.count('a'))
print(s.count('aa'))
print(s.count('a',3,7))    
