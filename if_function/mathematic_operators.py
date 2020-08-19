#program to find sum,sub,div,multiplication according to users choice
n1=int(input("Enter first Number:"))
n2=int(input("Enter second Number:"))
print("\t\t + \n\t\t - \n\t\t * \n\t\t /")
choice=input("Enter your choice:")
if choice=="+":
    print("Sum is:",n1+n2)
elif choice=="-":
    print("Substraction is:",n1-n2)
elif choice=="*":
    print("Multiplication is:",n1*n2)
elif choice=="/":
    print("Division is:",n1/n2)
else:
    print("Enter valid choice")
