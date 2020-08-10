list=[10,20,30]
print(list)
print(list[0])
print(list[-2])
print(list[1:3])

list[0]=100
for i in list:
    print(i)

list.append("ABC")
list.remove(20)
print(list)

list2=list*2
print(list2)
