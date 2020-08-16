def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print("factorial of 4 is:",factorial(4))
print("factorial of 5 is:",factorial(5))
