a,b=10,20
x=30 if a<b else 40
print(x)

#minimmum of 2 numbers
c=int(input("Enter First Number"))
d=int(input("Enter Second Number"))
min=c if c<d else d
print("Minimmum Value:",min)

#maximmum of 3 numbers
x=int(input("Enter First Number"))
y=int(input("Enter Second Number"))
z=int(input("Enter Third Number"))
max=x if x>y and x>z else y if y>z else z
print("Maximmum=",max)
