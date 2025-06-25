# Write a function clean_username(s) that strips leading/trailing spaces and lowercases the input. 
# Write a function snake_to_title(s) that converts "hello_world_test" → "Hello World Test". 
# Write a loop that prints each word in "devops is discipline" with its index using enumerate(). 
# Format this string using f-strings: name = "Keshin", role = "DevOps" → "Keshin is training as a DevOps warrior" 

def clean_username(s):
    return s.strip().lower()

print(clean_username("  sdfSDFSss  "))

def snake_to_title(s):
    s_out = ""
    lst = [word.capitalize() for word in s.split("_")] # I managed to use a list comprehension here! (proud)
    return " ".join(lst)


print(snake_to_title("hello_world_test"))

for i, word in enumerate("devops is discipline".split()):
    print(i, word)

name = "Keshan" 
role = "DevOps"
print(f"{name} is training as a {role} warrior")

#Write a function classify_score(score) that returns: "fail" if <50, "pass" if <85, "distinction" if 85+. 
#Write a function range_check(x) that returns True only if x is between 10 and 20 (inclusive). 
#Write a loop that finds the first number between 1 and 50 divisible by both 7 and 9. Use break. 
#Write a function is_palindrome(s) that checks whether a string is a palindrome (e.g. "racecar"). 

def classify_score(score):
    if score >= 85:
        return "distinction"
    elif score < 85 and score >= 50:
        return "pass"
    else:
        return "fail"

def range_check(x):
    return x >= 10 and x <= 20

for num in range(1,71): # The spec asks for 1 - 50 but this makes no sense as the first result is 63 ( out of the range )
    if num % 7 == 0 and num  % 9 == 0:
        print(num)
        break

def is_palindrome(s): # Tried to do this another way, seems to work..
    p1 = 0
    p2 = len(s) - 1

    for i in range(int(len(s) / 2)):
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True

print(is_palindrome("o"))

#Create a set from the list [1,2,2,3,4,4,5] and print it. 
#Given person = ("Alice", 30, "Tokyo"), unpack it and print: "Alice is 30 and lives in Tokyo" 
#Given a dict {"a": 1, "b": 2, "c": 3}, loop through its items and print key -> value 
#Create a function invert_dict(d) that flips keys and values. 
#Input: {"a": 1, "b": 2} → Output: {1: "a", 2: "b"} 

myset = set([1,2,2,3,4,4])
print(myset)


person = ("Alice", 30, "Tokyo")
(name, age, city) = person
print(f"{name} is {age} and lives in {city}")

dict = {"a": 1, "b": 2, "c": 3}

for k, v in dict.items():
    print(k, v)

def invert_dict(d):
    return {v: k for k,v in d.items()}

print(invert_dict(dict))