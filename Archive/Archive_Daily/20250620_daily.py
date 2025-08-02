#Use enumerate() to print each item and its index from a list of fruits.
#Use zip() to combine two lists (names and scores) and print them like "Alice scored 93"
#Loop through numbers 1–20 and print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both.
#Write a loop that prints a square (5x5) of alternating # and . characters like a checkerboard.

fruits = ['apple','banana','cherry']

for i,fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

names = ['andrew','bruce','charlie']
scores = [10,20,30]

for name, score in zip(names,scores):
    print(f"{name} scored {score}")

for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: FizzBuzz")
    elif i % 3 == 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")
    else:
        print(i)

for i in range(5):
    for j in range(5):
        offset = i + j
        print("#" if offset % 2 == 0 else ".", end="")
    print()


#Theme: Arguments, return values, and reusability
#
#Write a function multiply_or_add(x, y, *, op='multiply') that multiplies or adds based on the keyword argument.
#Write a function describe_person(name, age, city="Unknown") that returns a string like "Alice is 30 and lives in Tokyo".
#Write a function min_max_avg(lst) that returns the min, max, and average as a tuple.
#Write a function apply_to_all(func, lst) that applies a function to every element in a list and returns the result list.


def multiply_or_add(x, y , op='multiply'):
    if op == 'add':
        return x + y
    elif op == 'multiply':
        return x * y
    else:
        return "Unsupported operator: Please use multiply or add"
#TODO: Do error handling with exception and return none

        

def describe_person(name, age, city="Unknown"):
    return f"{name} is {age} and lives in {city}"

def min_max_avg(lst):
    min= lst[0]
    max = lst[0]
    avg_count = 0
    for num in lst:
        if num < min:
            min = num
        if num > max:
            max = num
        avg_count += num

    return (min,max,(avg_count / len(lst)))

lst = [2,4,2,5,7,8,8,2,12,5,1]

print(min_max_avg(lst))

def apply_to_all(func, lst):
    for item in lst:
        func(item)

