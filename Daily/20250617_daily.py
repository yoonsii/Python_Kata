# Use enumerate() to print each item and its index from a list of fruits.
# Use zip() to combine two lists (names and scores) and print them like "Alice scored 93"
# Loop through numbers 1–20 and print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both.
# Write a loop that prints a square (5x5) of alternating # and . characters like a checkerboard.

fruits = ['apple','banana','cherry','durian']

for i, f in enumerate(fruits):
    print(f"{i}, and fruit {f}")
