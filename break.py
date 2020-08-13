for i in range(10):
    if i==7:
        print("Please Break!")
        break
    print(i)

cart=[10,20,30,400,500]
for item in cart:
    if item>200:
        print("Parcel charge required")
        break
print(item)
