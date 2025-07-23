# Write a function count_uppercase(s) that counts how many uppercase letters are in s. 
# Write a function camel_to_snake(s) that converts camelCase to snake_case: 
# Example: "helloWorldTest" → "hello_world_test" 
# Given a sentence like "DevOps is discipline", write a loop that builds a list of word lengths. 
# Write a function starts_and_ends_same(s) that returns True if the first and last characters of s are the same (ignore case and spaces).
# Write a function manual_replace(s, old, new) that replaces all instances of old with new without using str.replace(). 


def count_uppercase(s):
    return sum(1 for c in s if c.isupper())

print(count_uppercase("Hey Guys hOw yo GOING"))


# Batch 2: Lists, Logic, and Reusability
# Write a function all_even(lst) that returns True if all elements in the list are even.
# Write a function filter_long_words(words, length) that returns only the words longer than length. Use a list comprehension.
# Write a function running_total(lst) that returns a list where each element is the sum of all previous elements plus itself.
#  Example: [1,2,3] → [1,3,6]
# Write a function find_max_index(lst) that returns the index of the largest element.
# Write a function apply_if(func, lst, condition) that applies func to each element only if it meets the condition. Use list comprehension.

def all_even(lst):
    return sum(lst) % 2 == 0

lst = [2,2,4,6,8,1]

print(all_even(lst))

def filter_long_words(words,length):
    return [word for word in words if len(word) > length]

w = ["a", "b", "cc", "dearie", "elephants"]

print(filter_long_words(w, 2))

lst = [1,2,3,4]

def running_total(lst):
    output = []
    for i, num in enumerate(lst):
        output.append(sum(lst[:num]))
    return output

print(running_total(lst))

def find_max_index(lst):
    return max(lst)

print(find_max_index(lst))

# However in the spirit of study I will do it manually as well
# Choosing not to sort as that may be computationally bad, whereas a single pass is only O(n)

def find_max_index_alt(lst):
    max = 0
    for i in lst:
        if i > max:
            max = i
    return max


