#### FILTER ##################

# Filter takes two arguments, returns an iterator (an object that can be traversed through)
# the first argument is a function
# second argument is a list

# Example: Filter out everything that isn't a multiple of 3 or 5 in a list of numbers.
def multiples_of_3_or_5(x):
    return x % 3 == 0 or x % 5 == 0

starting_list = range(3, 31)
filtered_list = list(filter(multiples_of_3_or_5, starting_list))

print("Multiples of 3 or 5: " + str(filtered_list))

# Challenge: create a filter function that only returns values
# between 10 and 20 along with values between 40 and 60
starting_list = range(0,100)

def f(x):
    return (x > 10 and x < 20) or (x > 40 and x < 60)

result = list(filter(f, starting_list))
print("Filter challenge result: " + str(result))


#### MAP ###############################################
# map() creates a mapping from each item in a list to the result of applying a function to each item
# map takes two arguments
# first arg is a function
# second arg is a list
# returns a map object that we can convert to a list

# Example: Map the numbers in a list to their squares

def to_squares(x):
    return x*x

items_to_square = range(1, 31)

squared_items = list(map(to_squares, items_to_square))
print("Squared Items = " + str(squared_items))

# Challenge: Map each name to a proper named format (capital first letter, lowercase other letters)
names = ['pHiLiP', 'gRaNt', 'jOhn', 'kAtniSS', 'lEslIe', 'miKasA', 'phIllIs']

def make_proper(name):
    return name.capitalize()

proper_names = list(map(make_proper, names))

print("Proper names: " + str(proper_names))


#### Reduce ##################################################

# reduce takes two arguments
# first arg: a function (that takes two arguments)
# second arg: a list
# reduce returns a single value

# How it works:
# First, it processes the first two items of the list using the function
# then, the result is processed with the next item in the list
# then that result is processed with the next item in the list,
# and so on...

from functools import reduce

# Example: Find the product of all the values in a list
values = range(1, 10)

def f(x,y):
    return x*y

result = reduce(f, values)
print("Product of list: " + str(result))

# Challenge: Use reduce to combine your first, middle, and last name, and any other names you may have.
names = ['Joshua', '"Josh"', 'Michael', 'Coriell', 'Eater of Tacos', 'Player of Saxophone', 'Mains Mercy', 'Not Kanye West']