# Introduction on Dictionary

# d = {'key': 'value'}

# user = {
#     'name': 'Abrar',
#     'age': 20
# }

# print(user)
# print(type(user))

# Access data from dictionary -

# user = {
#     'name': 'Abrar',
#     'age': 20
# }

# 1.
# print(user['name'])
# print(user['profession'])

# 2.
# print(user.get('name'))
# print(user.get('profession'))
# print(user.get('profession', None))
# print(user.get('profession', 'not found'))

# Add data to dictionary -

# user = {}

# user['name'] = 'Abrar'
# user['age'] = 20

# print(user)

# Conditionals and Looping

# user = {
#     'name': 'Abrar',
#     'age': 20
# }

# print(list(user.keys()))
# print(list(user.values()))
# print(list(user.items()))

# if 'profession' in user:
#     print(user.get('profession'))

# else:
#     print('No key found!')

# if 'Abrar' in user.values():
#     print('Found!')

# else:
#     print('Not found!')

# if 'Abrar' in user.keys():
#     print('Found!')

# else:
#     print('Not found!')

# user = {
#     'name': 'Abrar',
#     'age': 20
# }

# for loop

# for i in user:
#     print(i)

# for i in user.keys():
#     print(i)

# for i in user.values():
#     print(i)

# for i in user.items():
#     print(i)

# for key, value in user.items():
#     print(key, value)

# Delete data from dictionary -

# user = {
#     'name': 'Abrar',
#     'age': 20
# }

# user.pop('age') # Recommended

# popped_item = user.popitem()
# print(popped_item)

# print(user)

# Update Dictionary

# user = {
#     'name': 'Abrar',
#     'age': 20
# }

# other = {
#     'profession': 'Software Developer'
# }

# user.update(other)
# print(user)

# user = {}

# user.update(name='Amir', age=21, profession='Software Developer') # Recommended
# print(user)

# Common Methods

# user = {
#     'name': 'Abrar',
#     'age': 20
# }

# copied = user.copy()
# print(copied)

# user.clear()
# print(user)

# fromkeys() method

# user = dict.fromkeys(['name', 'age'])
# user = dict.fromkeys(['name', 'age'], None)
# user = dict.fromkeys(['name', 'age'], 'unknown')

# user = dict.fromkeys(['name', 'age'], input("Enter something : "))
# print(user)

# user.update(name=input("Name: "), age=input("Age: "))
# print(user)

# dict method

# user = dict()
# print(user)

# user = dict(name='Anshul', age=0, profession='Software Developer')
# print(user)

# Exercise - 1

# Define a function that takes a number n. It will return a dictionary
# having cube of numbers from 1 to n.

# d = {1: 1, 2: 8}

# def cube_finder(n):
#     cubes = {}

#     for i in range(1, n+1):
#         cubes[i] = i**3

#     return cubes

# print(cube_finder(2))

# Exercise - 2

# Define a function that takes your name. It will return a dictionary
# having a count of each character of your name.

# input = "Abrar"
# output = {'a': 2, 'b': 1, 'r': 2}

# def character_counter(name):
#     name = name.lower()
#     char_dict = {}

#     for ch in name:
#         char_dict[ch] = name.count(ch)

#     return char_dict

# print(character_counter(input("Enter your name: ")))
