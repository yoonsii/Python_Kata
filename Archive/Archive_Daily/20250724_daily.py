from collections import defaultdict
# Batch 3: Sets, Tuples, and Dictionaries
# Given ("John", "Smith", 30), unpack and print: "John Smith is 30 years old."
# Write a function unique_characters(s) that returns the set of unique characters in s.
# Write a function letter_frequency(s) that returns a dictionary of letter counts.
#  Example: "hello" → {'h':1, 'e':1, 'l':2, 'o':1}
# Write a function invert_dict(d) that swaps keys and values.
#  (e.g., {'a': 1, 'b': 2} → {1: 'a', 2: 'b'})
# Write a function dict_diff_keys(d1, d2) that returns the keys that are different between two dicts (i.e., keys that only exist in one or the other).

pack = ("John", "Smith", 30)

x, y, z = pack

print(x, y ,z)
print(x)

def unique_characters(s):
    return set(s)

def letter_frequency(s):
    output = defaultdict(int)
    for c in s:
        output[c] += 1
    return output

fruits = {"a":"apple", "b":"banana"}

def invert_dict(d):
    out = {}
    for key in d:
        print(key)
        out[d[key]] = key
    return out

print(list(fruits.keys()))

def dict_diff_keys(d1, d2):
    return set(list(d1.keys())).symmetric_difference(set(list(d2.keys())))

veggies = {"c":"cucumber", "d":"daikon", "a": "bapple"}

print(dict_diff_keys(fruits, veggies))


