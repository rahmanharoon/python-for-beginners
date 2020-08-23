class MySampleClass:
    def hello(self,n):
        self.name=n
        print("HELLO",n)
    def print_name(self):
        print("Name:",self.name)

x=MySampleClass()
y=MySampleClass()
name="RAHMAN HAROON"
x.hello(name)
y.hello("ROCKY")
x.print_name()
y.print_name()
