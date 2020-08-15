rec={}
n=int(input("Enter the number of strudents:"))
i=1
while i<=n:
    name=input("Enter Name of strudent:")
    mark=input("Enter % of mark:")
    rec[name]=mark
    i=i+1
    print("Name of strudent","\t","% of marks")
for x in rec:
    print("\t",x,"\t\t",rec[x])    
