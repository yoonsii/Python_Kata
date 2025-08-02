# Some practise to help me understand list comprehensions

# mylist = [1,3,5,6,7,3,12,4,11]

# for i in mylist:
#     print(i)

# newlist = [x * x for x in mylist if x > 10]

# print(newlist)


# Daily Practise
#Write a for loop to print numbers 1–5 using range().
#Write a while loop that prints numbers 0–4 using a break condition.
#Use a for loop with continue to skip printing the number 3 in a range.
#Write a nested loop to print a 3x3 grid of coordinates (e.g. 0,0 0,1 0,2...).


for i in range(1,6):
    print(i)

counter = 0

while True:
    if counter == 5:
        break
    print(counter)
    counter += 1

for i in range (10):
    if i == 3:
        continue
    print(i)

for i in range (3):
    for j in range(3):
        print(f"({i},{j})")

#Write a function square(n) that returns the square of a number.
#Write a function greet(name="warrior") that returns a greeting string.
#Write a function min_max(lst) that returns the min and max of a list.
#Write a recursive function factorial(n).
#Write a function apply_twice(func, x) that applies a function to a value twice.

def sqr(num):
    return num*num

def greet(name="warrior"):
    return f"Hello, {name}"

def min_max(list):
    return min(list), max(list)

def factorial(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num*factorial(num-1)
    
def applytwice(func, x):
    return func(func (x))



#Create a list of squares from 0 to 5 using list comprehension.
#Create a list of even numbers from 0 to 9 using list comprehension.
#Flatten a nested list [[1,2], [3,4]] using a nested list comprehension.
#Create a list that labels numbers 0–4 as "even" or "odd" using a conditional expression inside a comprehension.


mylist = [num * num for num in range(6)]
print(mylist)

myevenlist = [num for num in range (10) if num % 2 == 0]
print(myevenlist)