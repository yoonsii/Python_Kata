# Convert a list of integers to their string equivalents using map() and lambda.

x = lambda a : str(a)
lst = [1,2,3,4,7]

print(list(map(lambda a:str(a), lst)))