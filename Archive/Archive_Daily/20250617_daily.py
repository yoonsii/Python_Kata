# Use enumerate() to print each item and its index from a list of fruits.
# Use zip() to combine two lists (names and scores) and print them like "Alice scored 93"
# Loop through numbers 1–20 and print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both.
# Write a loop that prints a square (5x5) of alternating # and . characters like a checkerboard.

fruits = ['apple','banana','cherry','durian']

for i, f in enumerate(fruits):
    print(f"{i}, and fruit {f}")

scores = [55,66,77,88,91]
names = ['Anna','Bames','Charlie']

scores_and_list = zip(names,scores)

for thing in scores_and_list:
    print(f"{thing[0]} scores {thing[1]}")


for i in range(21):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"fizzbuzz")
    elif i % 3 == 0:
        print(i,"fizz")
    elif i % 5 == 0:
        print(i,"buzz")
    else:
        print(i)

for i in range(5):
    for j in range(5):
        total = i + j
        print("#" if total % 2 == 0 else ".", end="")
    print()