for i in range(6):
    print(i)

counter = 0
while True:
    if counter == 5:
        break
    print(counter)
    counter += 1


for i in range(5):
    if i == 3:
        continue
    print(i)

def sq(num):
    return num*num

def greet(name="warrior"):
    return f"Hi {name}"

def min_max(lst):
    return min(lst), max(lst)

def facto(num):
    if num == 0:
        return 1
    else:
        return num*facto(num - 1)

print (facto(5))

def applytwice(func, x):
    return func(func(x))

nums = [1,2,3,4,5]

sqlst = [num * num for num in nums]
print(sqlst)

evenlist = [num for num in range (10) if num % 2 == 0]
print(evenlist)

nestlist = [[1,2], [3,4]]
flattenlist = [num for nest in nestlist for num in nest]
print(flattenlist)

labels = ["even" if num % 2 == 0 else "odd" for num in range(5)]
print(labels)