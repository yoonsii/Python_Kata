# Convert a list of integers to their string equivalents using map() and lambda.

x = lambda a : str(a)
lst = [1,2,3,4,7]

print(list(map(lambda a:str(a), lst)))


# From a list of words, return only those with more than 4 characters.

x = lambda a : len(a) > 4
words = ["tree", "sunshine", "cat", "mountain", "sky", "apple"]

print(list(filter(x, words))) # could have put the function in here without a variable but am experimenting

# Exercise 3: Enumerate & Index Search
# Return the index of the first word in a list that starts with the letter "a".
words = ["sun", "cat", "apple", "banana", "avocado"]

def exercise_three(lst):
    for i, word in enumerate(words):
        if word.lower()[0] == "a":
            return i
    return

print(exercise_three(words))


names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

combined_names_scores = zip(names,scores)

# for x in combined_names_scores:
#     print(x[0])

output = [f"{x[0]}:{x[1]}" for x in combined_names_scores]
print(output)
