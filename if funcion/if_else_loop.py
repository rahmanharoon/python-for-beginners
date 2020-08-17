cart=[10,20,30,400,500]
for item in cart:
    if item>=400:
        print("WE cannot procces this item")
        break
    print(item)
else:
     print("Item proccessed succesfully..!")
