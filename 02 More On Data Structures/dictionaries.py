
# Dictionaries are sets of keys. Each key has a value associated with it.
# We says dictionaries are sets of key-value pairs
# keys are unique. values don't need to be unique

# Example of a dictionary: Info of a user

user = {
    'first_name': 'Josh',
    'last_name': 'Coriell',
    'zip_code': 71270
}

# Accessing the values
print("The user's info: ")
print(user['first_name'])
print(user['last_name'])
print()

# Changing values in the dictionary
user['zip_code'] = 70454
print("New Zip: ")
print(user['zip_code'])
print()


# Adding new items
user['middle_name'] = 'Michael'
print('Added middle name: ')
print(user['middle_name'])
print()

# Whole dictionary
print(user)

# Accessing the keys
for key in user:
    print(key)
print()

# accessing the values
for i in user:
    print(user[i])
print()

# accessing the keys using .keys()
for k in user.keys():
    print(k)
print()

# accessing the values using .items()
for k,v in user.items():
    print(f'{k} --> {v}')
print()


# Challenge:
# Given: A list of identically structured dictionaries,
#        each containing a 'first_name' and a 'last_name'.
# Create a function called combine_names that takes a user as input and returns their
#        first and last name combined
# use the map function to do it for all of the users



users = [
    {'first_name': 'Ann', 'last_name': 'Perkins'},
    {'first_name': 'Britta', 'last_name': 'Perry'},
    {'first_name': 'Eren', 'last_name': 'Jaeger'},
    {'first_name': 'Shotgun', 'last_name': 'Shootyman'},
    {'first_name': 'Cowboy', 'last_name': 'Keychainman'}
]


def combine_names(user):
    return user['first_name'] + ' ' + user['last_name']

result = list(map(combine_names, users))

print(result)





