from collections import defaultdict
# Batch 1: Strings, Loops, and Conditionals 
# Write a function camel_to_snake(s) that converts camelCase to snake_case: 
# Example: "helloWorldTest" → "hello_world_test" 
# Given a sentence like "DevOps is discipline", write a loop that builds a list of word lengths. 
# Write a function starts_and_ends_same(s) that returns True if the first and last characters of s are the same (ignore case and spaces). 
# Write a function manual_replace(s, old, new) that replaces all instances of old with new without using str.replace(). 


def camel_to_snake(s):
    return "".join(f"_{c.lower()}" if c.isupper() else c for c in s  )

print(camel_to_snake("thisIsCamelCase"))

str = "DevOps is discipline"

lengths = [len(word) for word in str.split()]
print(lengths)

def starts_and_ends_same(s):
    s = s.trim().lower()
    return s[0] == s[-1] if s else False

def manual_replace(s, old, new):       
    while(s.find(old) != -1):
        print(s[:s.find(old)])
        s = s[:s.find(old)] + new + s[s.find(old) + len(old):]
    return s
str = "This is a stringis"
    
print(manual_replace(str, "is", "zzz"))


 

# Batch 2: Lists, Logic, and Reusability 
# Write a function all_even(lst) that returns True if all elements in the list are even. 
# Write a function filter_long_words(words, length) that returns only the words longer than length. Use a list comprehension. 
# Write a function running_total(lst) that returns a list where each element is the sum of all previous elements plus itself. 
# Example: [1,2,3] → [1,3,6] 
# Write a function find_max_index(lst) that returns the index of the largest element. 
# Write a function apply_if(func, lst, condition) that applies func to each element only if it meets the condition. Use list comprehension. 

lst = [2,4,6,2,4,7,7,6,8]

def all_even(lst):
    for x in lst:
        if x % 2 == 1:
            return False
    return True

print(all_even(lst))

lst = ["a","bb","ccc","dddd","eeeee"]

def filter_long_words(words,length):
    return [word for word in words if len(word) > length]

print(filter_long_words(lst, 3))

def running_total(lst):
    count = 0
    output = []
    for x in lst:
        count += x
        output.append(count)
    return output

lst = [1,2,3]

print(running_total(lst))

def find_max_index(lst):
    max = 0
    for x in lst:
        if x > max:
            max = x
    return max

#alternatively could use max() but defeats the purpose of learning here

def apply_if(func, lst, condition):
    return [func(item) for item in lst if condition(item)]

# I don't fully understand this and would appreciate a lesson/example of this in use and why it would be used.

# Batch 3: Sets, Tuples, and Dictionaries 
# Write a function letter_frequency(s) that returns a dictionary of letter counts. 
# Example: "hello" → {'h':1, 'e':1, 'l':2, 'o':1} 
# Write a function invert_dict(d) that swaps keys and values. 
# (e.g., {'a': 1, 'b': 2} → {1: 'a', 2: 'b'}) 
# Write a function dict_diff_keys(d1, d2) that returns the keys that are different between two dicts (i.e., keys that only exist in one or the other). 

def letter_frequency(s):
    frequency_dict = defaultdict(int)
    for c in s:
        frequency_dict[c] += 1
    return frequency_dict

print(letter_frequency("hello"))

d = {'a':1, 'b':2}

def invert_dict(d): # the spec for this doesn't specify whether to output a new dict or swap in original - I'm assuming new dict
    output = {}
    for key in d.keys():
        output[d[key]] = key

    return output

print(invert_dict(d))

fruits = {"a":"apple", "b":"banana"}
veggies = {"c":"cucumber", "d":"daikon", "a": "apple"}


def dict_diff_keys(d1,d2):
    return(set(d1.keys()).symmetric_difference(set(d2.keys())))

print(dict_diff_keys(fruits,veggies))
