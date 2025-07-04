#Use enumerate() to print each item and its index from a list of fruits.
#Use zip() to combine two lists (names and scores) and print them like "Alice scored 93"
#Loop through numbers 1–20 and print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both.
#Write a loop that prints a square (5x5) of alternating # and . characters like a checkerboard.

fruits = ['apples','banana','cherry']

for i,f in enumerate(fruits):
    print(f"{i}: {f}")

names = ['Alice','Bob','Charlie']
scores = [23,45,91]

if len(names) != len(scores):
    print(f"Warning: length mismatch in lists")

for n,s in zip(names,scores):
    print(f"{n} scored {s}")

for i in range(1,21):
    if i % 5 == 0 and i % 3 == 0:
        print(f"{i}: FizzBuzz")
    elif i % 3 == 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")

for i in range(5):
    for j in range(5):
        total = i + j
        print("#" if total % 2 == 0 else ".", end="")
    print()


#Theme: Arguments, return values, and reusability

#Write a function multiply_or_add(x, y, *, op='multiply') that multiplies or adds based on the keyword argument.
#Write a function describe_person(name, age, city="Unknown") that returns a string like "Alice is 30 and lives in Tokyo".
#Write a function min_max_avg(lst) that returns the min, max, and average as a tuple.
#Write a function apply_to_all(func, lst) that applies a function to every element in a list and returns the result list.

def multiply_or_add(x, y, *, op='multiply'):
    if op == 'multiply':
        return x * y
    elif op == 'add':
        return x + y
    else:
        raise ValueError("Incompatible Operator. Usage: (x, y, multiply/add)")

def describe_person(name, age, city="Unknown"):
    return f"{name} is {age} and lives in {city}"

def min_max_avg(lst):
    return (min(lst), max(lst), sum(lst)/len(lst))

def apply_to_all(func, lst):
    return [func(item) for item in lst]



#Theme: Filtering, transformation, and complexity

#Create a list of the squares of all even numbers between 1 and 20 using list comprehension.
#Create a list of all 3-letter words from ["cat", "apple", "dog", "banana", "ant"] using a list comprehension.
#Build a dictionary using dict comprehension where keys are numbers 1–5 and values are their cubes.
#Use list comprehension to flatten [[1,2,3],[4,5],[6]] into [1,2,3,4,5,6]

lst = [num for num in range(1,21) if num % 2 == 0]

words = ["cat", "apple", "dog", "banana", "ant"]

lst = [word for word in words if len(word) == 3]


d = {i: i ** 3 for i in range(1,6)}

for key in d:
    print(key, d[key])

unflatten = [[1,2,3],[4,5],[6]]

lst = [num for sublist in unflatten for num in sublist]