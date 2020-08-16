a=100
def a():
    global a
    a=212
    print(a)

def b():
    print(a)

a()
b()        
