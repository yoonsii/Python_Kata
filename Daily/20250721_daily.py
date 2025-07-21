# Write a function count_uppercase(s) that counts how many uppercase letters are in s. 
# Write a function camel_to_snake(s) that converts camelCase to snake_case: 
# Example: "helloWorldTest" → "hello_world_test" 
# Given a sentence like "DevOps is discipline", write a loop that builds a list of word lengths. 
# Write a function starts_and_ends_same(s) that returns True if the first and last characters of s are the same (ignore case and spaces).
# Write a function manual_replace(s, old, new) that replaces all instances of old with new without using str.replace(). 

def count_uppercase(s):
    return sum(1 for c in s if c.isupper())

print(count_uppercase("helLLo ThiS is uPPer"))

def camel_to_snake(s):
    