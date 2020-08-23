class MySampleClass:
    year=2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1
    def relocate(self,place):
        self.place=place
    def display(self):
        print("Year:",str(MySampleClass.year))
        print("Name:",self.name)
        print("Age:",str(self.age))
        print("Place:",self.place)
    @classmethod
    def add_year(cls):
        cls.year=cls.year+1
x=MySampleClass("Rahman Haroon",22,"Kannur")
y=MySampleClass("RAHMAN HAROON",22,"KANNUR")
x.display()
y.display()
print("----------------------------")
MySampleClass.year=MySampleClass.year+1
x.add_age()
y.add_age()
x.display()
y.display()
print("----------------------------")
MySampleClass.add_year()
x.add_age()
y.add_age()

x.relocate("Calicut")
y.relocate("Kochi")

x.display()
y.display()
