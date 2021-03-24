
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



