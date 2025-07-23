# Batch 1: Working with Strings & Loops
# Write a function remove_vowels(s) that returns the string with all vowels removed.
# Write a loop that counts how many digits are in a string like "abc123de45" (hint: char.isdigit()).
# Write a function alternate_case(s) that returns the input string with alternating letter casing: "hello" → "HeLlO".
# Write a loop that builds a new string by reversing "devopswarrior" using a loop (no slicing).

def remove_vowels(s):
    return "".join(c for c in s if c.lower() not in "aeiou")

print(remove_vowels("Hey How are you"))

for i in "abc123de45":
    count = sum(1 for i in "abc12de45" if i.isdigit())

print(count)

def alternate_case(s):
    return "".join(c.capitalize() if i % 2 == 0 else c for i,c in enumerate(s))

print(alternate_case("Hey guys how's EveryBody doing?"))

def reverse(s):
    return reversed(s)
    # Need to remember this returns an iterator not a string so we need to join

# but also to understand the concepts I'll do it the other way too

def reverse_manual(s):
    out = ""
    for i in range(len(s) - 1, -1, -1):
        out += s[i]
    return out

print(reverse_manual("devopswarrior"))

# but then again I'm lerning bout comprehensions and generators sooo.. lets odo this to

def reverse_expression(s):
    return "".join(s[i] for i in range(len(s) -1, -1, -1))

print(reverse_expression("devopswarriior"))


# Batch 2: List Practice – Search & Transformation
# Write a function find_first_even(lst) that returns the first even number from the list, or None if not found.
# Write a function double_until_threshold(lst, threshold) that multiplies each number by 2 until the first one exceeds the threshold — then stop and return the new list.
# Given a list [" apple ", "banana ", " cherry"], strip all whitespace and capitalize each word. Use list comprehension.
# Write a function flatten_and_square(matrix) that flattens a list of lists and returns the square of each number.

def find_first_even(lst):
    for i in lst:
        if i % 2 == 0:
            return i
    return


# assume I can use some kind of list comprehension here but not sure how to do it with return if possible
# will just complete the exercise then ask for feedback afterwards

def double_until_threshold(lst, threshold):
    newlist = []
    for i in lst:
        newlist.append(i * 2)
        if i * 2 > threshold:
            return newlist
        
lst = [" apple ", "banana ", " cherry"]

lst = [word.strip().capitalize() for word in lst]

print(lst)

matrix = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

lst = [num ** 2 for sublist in matrix for num in sublist]

print(lst)

# Batch 3: Booleans, Membership, and Sets
# Write a function has_duplicates(lst) that returns True if the list has any duplicates.
# Given s1 = "hello", s2 = "world", write a function common_letters(s1, s2) that returns a set of letters they share.
# Write a function is_subset(small, big) that returns True if all elements in small are in big. Use set logic.
# Given a list of names, remove duplicates and sort them alphabetically.

lst = [1,2,3,4,4,5]

def has_duplicates(lst):
    return not len(lst) == len(set(lst))

# Thinking about doing this algorithmically I can only think of checking each elem against each other 
# which I think would result in O(n^2)

s1 = "hello" 
s2 = "world"

def common_letters(s1, s2):
    return set("".join(c for c in s1 if c in s2))

print(common_letters(s1,s2))

# Still learning but just a note: I'll work on doing these pythonically and when I start doing c++ I can focus on
# the more algorithmic ways of doing things

def is_subset(small,big):
    return small.issubset(big)


lst = ['alice','bob','damien','charlie','charlie']

# removing duplicates
def remove_duplicate(lst):
    lst.sort()
    print(lst)
    return set(lst)

print(remove_duplicate(lst))

# seems that when I run this multiple times the resulting set is in different orders at different times. why?

    
    