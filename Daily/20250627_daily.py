# Batch 1: Working with Strings & Loops
# Write a function remove_vowels(s) that returns the string with all vowels removed.
# Write a loop that counts how many digits are in a string like "abc123de45" (hint: char.isdigit()).
# Write a function alternate_case(s) that returns the input string with alternating letter casing: "hello" → "HeLlO".
# Write a loop that builds a new string by reversing "devopswarrior" using a loop (no slicing).

def remove_vowels(s):
    return "".join(c for c in s if c.lower() not in "aeiou")

count = 0
for i in "abc123de45":
    count += 1 if i.isdigit() else 0 # trying new things not sure if this is the 'proper' way to do this

# Better python idiom
# count = sum(1 for i in "abc123de45" if i.isdigit())


print(count)

# def alternate_case(s):
    # out = ""
    # for i,c in enumerate(s):
        # out += c.capitalize() if i % 2 == 0  else c
    # return out

def alternate_case(s):
    s = s.lower()

    return "".join(c.upper() if i % 2 == 0 else c for i,c in enumerate(s))

print(alternate_case("Hello How ARE You"))

def reverse_string(s):
    return ''.join(reversed(s))

print(reverse_string('devopswarrior'))


# Batch 2: List Practice – Search & Transformation
# Write a function find_first_even(lst) that returns the first even number from the list, or None if not found.
# Write a function double_until_threshold(lst, threshold) that multiplies each number by 2 until the first one exceeds the threshold — then stop and return the new list.
# Given a list [" apple ", "banana ", " cherry"], strip all whitespace and capitalize each word. Use list comprehension.
# Write a function flatten_and_square(matrix) that flattens a list of lists and returns the square of each number.

def find_first_even(lst):
    for i in lst:
        if i.isdigit() and i % 2 == 0:
            return i
    return


# Batch 3: Booleans, Membership, and Sets
# Write a function has_duplicates(lst) that returns True if the list has any duplicates.
# Given s1 = "hello", s2 = "world", write a function common_letters(s1, s2) that returns a set of letters they share.
# Write a function is_subset(small, big) that returns True if all elements in small are in big. Use set logic.
# Given a list of names, remove duplicates and sort them alphabetically.
