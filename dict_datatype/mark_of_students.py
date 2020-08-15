n=int(input("Enter no of students:"))
d={}
for i in range(n):
    name=input("Enter Srudent name:")
    marks=input("Enter student marks:")
    d[name]=marks
    while True:
        name=input("ENter student name to get marks:")
        marks=d.get(name,-1)
        if marks==-1:
            print("Student Not found")
        else:
            print("Marks of",name,"are",marks)
        option=input("Do you want to find another student marks[yes\no]")
        if option=="No":
            break
    print("Thank you")
print("Thanks for using our application")
