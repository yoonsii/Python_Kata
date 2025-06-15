# Print all odd numbers from 1–10 using a for loop and continue.
# Use a while loop to print numbers from 10 to 1, skipping number 5.
# Write a loop that sums numbers from 1 to 100 and prints the result.
# Print a right-angled triangle of stars (*) 5 lines tall using nested loops:

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

counter = 10
while counter > 0:
    if counter != 5:
        print(counter)
    counter -= 1

sum = 0
for i in range(101):
    sum = sum + i
print(sum)

for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()

# Write a function is_even(n) that returns True if a number is even.
# Write a function count_evens(lst) that returns how many even numbers are in a list.
# Write a function reverse_string(s) that returns the reversed version of the string.
# Write a function sum_of_squares(lst) that returns the sum of all squares in a list.
# Write a function fibonacci(n) that returns the nth Fibonacci number using recursion.

def is_even(n):
    return n % 2 == 0

lst = [5,3,2,2]

def count_evens(lst):
    counter = 0
    for num in (lst):
        if is_even(num):
            counter += 1
    return counter

print(count_evens(lst))

def reverse_string(s):
    return s[::-1]

def sum_of_squares(lst):
    counter = 0
    for num in lst:
        counter += num**2
    return counter

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# Create a list of squares from 0 to 5 using list comprehension.
# Create a list of even numbers from 0 to 9 using list comprehension.
# Flatten a nested list [[1,2], [3,4]] using a nested list comprehension.
# Create a list that labels numbers 0–4 as "even" or "odd" using a conditional expression inside a comprehension.

lst = [num * num for num in range(6)]

lst = [num for num in range(10) if num % 2 == 0]

mylst = [[1,2], [3,4]]

lst = [num for sublist in mylst for num in sublist]
print(lst)

lst = ["even" if num % 2 == 0 else "odd" for num in range(5)]
print(lst)