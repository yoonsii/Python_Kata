# Batch 1: String Manipulation & Formatting

# Write a function clean_username(s) that strips leading/trailing spaces and lowercases the input.
# Write a function snake_to_title(s) that converts "hello_world_test" → "Hello World Test".
# Write a loop that prints each word in "devops is discipline" with its index using enumerate().
# Format this string using f-strings: name = "Keshin", role = "DevOps" → "Keshin is training as a DevOps warrior"

def clean_usernames(un):
  return un.strip().lower()
 
print(clean_usernames("   sksSjsHhH.  "))

def snake_to_title(s):
  words = s.split("_")
  for w in words:
    w.capitalize()
    
  words = " ".join(words)
  return words
    
temp = "what_is_this"
print(snake_to_title(temp))


for i,w in enumerate(("devops is discipline").split()):
  print(i,w)

name = "Keshan"
role = "DevOps"
print(f"{name} is training as a {role} warrior")

# Batch 2: Logic, Branching, and Realistic Thinking

# Write a function classify_score(score) that returns: "fail" if <50, "pass" if <85, "distinction" if 85+.
# Write a function range_check(x) that returns True only if x is between 10 and 20 (inclusive).
# Write a loop that finds the first number between 1 and 50 divisible by both 7 and 9. Use break.
# Write a function is_palindrome(s) that checks whether a string is a palindrome (e.g. "racecar").

def classify_score(score):
  if score >= 85:
    return "distinction"
  elif score < 85 and score >= 50:
    return "pass"
  elif score < 50:
    return "fail"

def range_check(x):
  return x >= 10 and x <= 20

for i in range(1,51):
  if i % 7 == 0 and i % 9 == 0:
    print(i)
    break
  
def is_palindrome(s):
    p1 = 0
    p2 = len(s) - 1

    for i in range(len(s)):
        if p1 < p2:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
               return False
        else:
           return True
        
# it only returns True if it survives the entire loop. 
# As written, it returns True too early if the pointers cross during the loop. Also, could exit early if len(s) is 0 or 1.

# def is_palindrome(s):
#     p1 = 0
#     p2 = len(s) - 1

#     while p1 < p2:
#         if s[p1] != s[p2]:
#             return False
#         p1 += 1
#         p2 -= 1
#     return True

print(is_palindrome("raccooar"))

# Batch 3: Data Structures – Sets, Tuples, and Dicts

# Create a set from the list [1,2,2,3,4,4,5] and print it.
# Given person = ("Alice", 30, "Tokyo"), unpack it and print: "Alice is 30 and lives in Tokyo"
# Given a dict {"a": 1, "b": 2, "c": 3}, loop through its items and print key -> value
# Create a function invert_dict(d) that flips keys and values.
# Input: {"a": 1, "b": 2} → Output: {1: "a", 2: "b"}

lst = [1,2,2,3,4,4,5] 
myset = set(lst)

person = ("Alice", 30, "Tokyo")
(name, age, city) = person

print(f"{name} is {age} and lives in {city}")

dict = {"a": 1, "b": 2, "c": 3}

# There is a better way to do this for k, v in dict.items you suggested but I'm unsure of how to use this idiom
for key in dict:
   print(dict[key])

def invert_dict(d):
    new_dict = {}
    for key in d:
        new_dict[d[key]] = key

    return new_dict

d1 = {"a": 1, "b": 2}

d2 = {}
d2 = invert_dict(d1)

for key in d2:
   print(key, d2[key])

  
 
  
 
  


