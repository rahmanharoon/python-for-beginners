word=input("Enter the word:")
vowels={'a','e','i','o','u'}
d={}
for x in words:
    if x in vowels:
        d[x]=d.get(x,0)+1
    for k,v in sorted(d.items()):
        print(k,"occured",v,"times")
