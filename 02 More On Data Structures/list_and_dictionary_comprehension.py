# list and dictionary comprehension

# list comprehension

squares = [x*x for x in range(1,20)]
print(squares)

# with a conditional
vowels = [letter for letter in 'how are you?' if letter in 'aeiou']
print(vowels)

# multiple loops
products = [f'{x} * {y} = {x*y}' for x in range(1, 10) for y in range(1, 10)]
print(products)

[print(product) for product in products]