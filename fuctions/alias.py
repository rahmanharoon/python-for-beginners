def wish(name):
    print("Good Mornig:",name)
greeting=wish
print(id(wish))
print(id(greeting))

greeting('ROCKY')
wish('ROCKY bai')
