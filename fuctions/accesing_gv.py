a=100
def f():
    a=121
    print(a)
    print(globals()['a'])

f()
