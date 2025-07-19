# Batch 1: Working with Strings & Loops
# Write a function remove_vowels(s) that returns the string with all vowels removed.
# Write a loop that counts how many digits are in a string like "abc123de45" (hint: char.isdigit()).
# Write a function alternate_case(s) that returns the input string with alternating letter casing: "hello" → "HeLlO".
# Write a loop that builds a new string by reversing "devopswarrior" using a loop (no slicing).

def remove_vowels(s):
    return "".join(c for c in s if c.lower() not in "aeiou")

print(remove_vowels("Hey How are you"))

for i in "abc123de45":
    count = sum(1 for i in "abc12de45" if i.isdigit())

print(count)

def alternate_case(s):
    return "".join(c.capitalize() if i % 2 == 0 else c for i,c in enumerate(s))

print(alternate_case("Hey guys how's EveryBody doing?"))

def reverse(s):
    return "".join(reversed(s))

print(reverse("devopswarrior"))

# Batch 2: List Practice – Search & Transformation
# Write a function find_first_even(lst) that returns the first even number from the list, or None if not found.
# Write a function double_until_threshold(lst, threshold) that multiplies each number by 2 until the first one exceeds the threshold — then stop and return the new list.
# Given a list [" apple ", "banana ", " cherry"], strip all whitespace and capitalize each word. Use list comprehension.
# Write a function flatten_and_square(matrix) that flattens a list of lists and returns the square of each number.

lst = [1,5,7,3]

def find_first_even(lst):
    for d in lst:
        if d % 2 == 0:
            return d
    return

print(find_first_even(lst))

def double_until_threshold(lst, threshold):
    result = []
    for num in lst:
        doubled = num * 2
        if doubled > threshold:
            break
        result.append(doubled)
    return result

lst =  [" apple ", "banana ", " cherry"]

new_lst = [word.lower().strip().capitalize() for word in lst]

print(new_lst)

matrix = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

def flatten_and_square(lst):
    return [num for sublist in lst for num in sublist]

print(flatten_and_square(matrix))




# Batch 3: Booleans, Membership, and Sets
# Write a function has_duplicates(lst) that returns True if the list has any duplicates.
# Given s1 = "hello", s2 = "world", write a function common_letters(s1, s2) that returns a set of letters they share.
# Write a function is_subset(small, big) that returns True if all elements in small are in big. Use set logic.
# Given a list of names, remove duplicates and sort them alphabetically.



    
    