#Write a function remove_vowels(s) that returns the string with all vowels removed. 
#Write a loop that counts how many digits are in a string like "abc123de45" (hint: char.isdigit()). 
#Write a function alternate_case(s) that returns the input string with alternating letter casing: "hello" → "HeLlO". 
#Write a loop that builds a new string by reversing "devopswarrior" using a loop (no slicing). 

def is_vowel(s):
    return s in "aeiouAEIOU"

def remove_vowels(s):
    out = ""
    for c in s:
        if not is_vowel(c):
            out += c
    return out

print(remove_vowels("Hello please remove the vowels"))

count = 0
for c in "abc123de45":
    if c.isdigit():
        count += 1

print(count)

def alternate_case(s):
    s = s.lower()
    out = ""
    for i,c in enumerate(s):
        out += c.capitalize() if i % 2 == 0  else c
    return out

print(alternate_case("Hello What to Do"))

out = ""
phrase = "devopswarrior"
for c in range(len(phrase) - 1, -1,-1):
    print(c)
    print(phrase[c])
    out += phrase[c]
print(out)

    


