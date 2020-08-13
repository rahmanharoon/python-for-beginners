for i in range(20):
    if i%2==0:
        continue
    print(i)

cart=[10,20,30,400,500,600]
for item in cart:
    if item<400:
        print("Parcel charge requires",item)
        continue
    print(item)
