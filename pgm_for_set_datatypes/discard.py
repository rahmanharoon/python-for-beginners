#It removes the specified element from the set.
s={10,20,30,400}
print(s)
s.discard(400)
print(s)
#If the specified element not present in the set then we won't get any error.
s.discard(100)
print(s)
