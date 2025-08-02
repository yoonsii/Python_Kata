for i in range(1,6):
    print(i)

counter = 0

while counter < 5:
    print(counter)
    counter += 1
    

for i in range(6):
    if i == 3:
        continue
    print(i)

for i in range (4):
    for j in range(4):
        print(f"({i},{j})")

# Wrte a function that returns the square of a number

def sq(num):
    return num*num
# I think this is clearer than num**2 perhaps?

print (sq(9))

def greet(name="warrior"):
    print(f"hello {name}")

greet()

thislist = [3,7,4,2,12,1,5]

# day 1 using naive methods to complete this. From tomorrow will use better methods
thislist.sort()
print(thislist)
print(min(thislist))
print(max(thislist))

def facto(num):
    if num == 1: 
        return 1
    return num*facto(num -1)

print (facto(5))

stor = 0

def add3(num):
    return num + 3

def applytwice(func, x):
    return func(func (x))

print(applytwice(add3, 5))



