# Some practise to help me understand list comprehensions

mylist = [1,3,5,6,7,3,12,4,11]

for i in mylist:
    print(i)

newlist = [x * x for x in mylist if x > 10]

print(newlist)