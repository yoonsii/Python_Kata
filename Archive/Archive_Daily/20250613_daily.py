# Print all odd numbers from 1–10 using a for loop and continue.
# Use a while loop to print numbers from 10 to 1, skipping number 5.
# Write a loop that sums numbers from 1 to 100 and prints the result.
# Print a right-angled triangle of stars (*) 5 lines tall using nested loops:

for i in range(11):
    if i % 2 == 0:
        continue
    else:
        print(i)

counter = 10
while counter > 0:
    if counter != 5:
        print(counter)
    counter -= 1

sum = 0
for i in range(101):
    sum = sum + i

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
    if n % 2 == 0:
        return True
    else:
        return False

def count_evens(lst):
    count = 0
    for num in lst:
        if is_even(num):
            count += 1
    return count

testlist = [1,2,2,5,6,3,5,7,3,2,4,10]

def reverse_string(s):
    rstring = ""
    for i in range(len(s), 0, -1):
        print(i)
        rstring += s[i - 1]
    
    return rstring

def sum_of_squares(lst):
    sum = 0
    for num in list:
        sum += (num * num)        

def fibonacci(n):
    if n == 1:
        return 1
    else:
        return n + (fibonacci(n - 1))
    


# Create a list of squares from 0 to 5 using list comprehension.
# Create a list of even numbers from 0 to 9 using list comprehension.
# Flatten a nested list [[1,2], [3,4]] using a nested list comprehension.
# Create a list that labels numbers 0–4 as "even" or "odd" using a conditional expression inside a comprehension.

lst = [num * num for num in range(6)]
print(lst)

lst = [num for num in range(10) if num % 2 == 0]
print(lst)

inputlist = [[1,2], [3,4]] 
lst = [num for slist in inputlist for num in slist]
print(lst)

lst = ["even" if num % 2 == 0 else "odd" for num in range(5)]
print(lst)

# Mystery meat

def z(n):
    t = 0
    a = 1
    b = 1
    x = 2
    if n == 0:
        return 0
    while x <= n:
        c = a + b
        a = b
        b = c
        t += c
        x += 1
    return t + 2

# Didn't get this one! This is the fibbonacci sequence 