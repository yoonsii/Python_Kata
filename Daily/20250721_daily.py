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
    output = []
    for c in s:
        if c.islower():
            output.append(c)
        else:
            output.append(f"_{c}")
    return "".join(output).lower()

print(camel_to_snake("helloThisIsCamelCase"))

wordcount = []
ss = "DevOps is disciplineD"
for word in ss.split():
    print(word)
    wordcount.append(len(word))

print(wordcount)

def starts_and_ends_same(s):
    return ss[0] == ss[-1]
    
print(starts_and_ends_same(ss))

def manual_replace(s, old, new):
    posn = s.find(old)
    while(posn > -1):
        output = rep_str[:posn] + new + rep_str[posn + len(new):]
        posn = s.find(old)
    return output
    


rep_str = "Hi this is a string"

# print(rep_str.find("is"))
# findpos = rep_str.find("is")

# print(rep_str[:findpos])
# print(rep_str[findpos + len("is"):])

print(manual_replace(rep_str, "is","xx"))

    