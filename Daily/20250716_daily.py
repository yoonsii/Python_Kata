# Write a function remove_vowels(s) that returns the string with all vowels removed. 
# Write a loop that counts how many digits are in a string like "abc123de45" (hint: char.isdigit()). 
# Write a function alternate_case(s) that returns the input string with alternating letter casing: "hello" → "HeLlO". 
# Write a loop that builds a new string by reversing "devopswarrior" using a loop (no slicing). 

def remove_vowels(s):
    return "".join(c for c in s.lower() if c not in "aeiou")

print(remove_vowels("Hey look at this"))

ss = "abc123de45"

print(sum(1 for c in ss if c.isdigit()))

def alternate_case(s):
    return "".join(c if i % 2 == 0 else c.lower() for i, c in enumerate(s.upper()) )

print(alternate_case("Hey Hello My friend"))

ss = "devopswarrior"





# Batch 2: List Practice – Search & Transformation 
# Write a function find_first_even(lst) that returns the first even number from the list, or None if not found. 
# Write a function double_until_threshold(lst, threshold) that multiplies each number by 2 until the first one exceeds the threshold — then stop and return the new list. 
# Is it possible to do this in a comprehension 
# Given a list [" apple ", "banana ", " cherry"], strip all whitespace and capitalize each word. Use list comprehension. 
# Write a function flatten_and_square(matrix) that flattens a list of lists and returns the square of each number. 

 

# Batch 3: Booleans, Membership, and Sets 
# Write a function has_duplicates(lst) that returns True if the list has any duplicates. 
# Given s1 = "hello", s2 = "world", write a function common_letters(s1, s2) that returns a set of letters they share. 
# Write a function is_subset(small, big) that returns True if all elements in small are in big. Use set logic. 
# Given a list of names, remove duplicates and sort them alphabetically. 