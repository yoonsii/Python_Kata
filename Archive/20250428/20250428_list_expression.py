conf_pairs = {"a":"aardvark", "b":"banana", "ccc":"cherry"}

valid_keys = ['a','banana','ccc']

output = []

# Testing logic
for word in valid_keys:
    if word not in conf_pairs:
        output.append(word)

output_comprehension = [word for word in valid_keys if word not in conf_pairs]


print(output)
print(output_comprehension)