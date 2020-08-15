word=input("Enetr a word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,'occured',v,'times')    
