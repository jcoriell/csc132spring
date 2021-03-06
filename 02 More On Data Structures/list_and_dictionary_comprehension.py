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


#### Dictionary Comprehension ########
# Example:

values = {x: x**2 for x in range(10)}

print(values)
print(values[3])

##### Challenges ##############

## Challenge: Use list comp to create a list of numbers divisible by 3 or 5 (up to 30)
# print the list

multiples = [x for x in range(3, 31) if x % 3 == 0 or x % 5 == 0]
print(multiples)