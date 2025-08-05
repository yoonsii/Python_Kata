from utils_20250805 import sum_all
# 6. Basic Arg Unpacking
# Function that returns the sum of any number of args using *argso

# def sum_all(*args): #commented for #8
#     count = 0
#     for i in args:
#         count += i
#     return count

# print(sum_all(1,2,3,7))

# 7. Kwarg Info Formatter
# Function that accepts **kwargs and prints nicely formatted key:value pairs

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} --> {value}")

print_info(name="Alice", age=30, job="Engineer")

# 8. Refactor into Module
# Move a utility function into a separate .py file and import it

print(sum_all(2,4,6,8))

# 9. Tuple Unpacking Puzzle
# Extract all names from [("John", 25), ("Jane", 30), ...]

people = [("John", 25), ("Jane", 30), ("Alice", 28), ("Bob", 40)]

lst = [name for name, age in people]

print(lst)

# 10. Dict Merge Tool
# Merge two kwargs-style dicts using ** unpacking