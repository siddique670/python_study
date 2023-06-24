# Introduction To Functions

# A piece of code

# 1. Function Definition
# 2. Function Calling

# Naming Coventions -

# 1. Snake Case (Recommended for python - for variable and function)
# 2. Camel Case (Recommended for java - for variable and function)
# 3. Pascal Case (Both - for class names)

# def hello_world():
#     print("Hello World")

# hello_world()

# def sum_of_two_numbers(number_1, number_2):
#     print(number_1 + number_2)

# sum_of_two_numbers(1, 2)
# sum_of_two_numbers(2, 3)
# sum_of_two_numbers(3, 4)
# sum_of_two_numbers(4, 5)

# * Function must return some value otherwise their will be no use of function.

# def sum_of_numbers(n):
#     total = 0

#     for i in range(1, n+1):
#         total += i

#     print(total) # It will not return any value

# a = sum_of_numbers(100)
# print(a) # None

# Recommended

# def sum_of_numbers(n):
#     total = 0

#     for i in range(1, n+1):
#         total += i

#     return total

# a = sum_of_numbers(100)
# print(a)

# def sum_of_numbers(n):
#     total = 0

#     for i in range(1, n+1):
#         total += i

#     return total

# num = int(input("Enter a number: "))
# print(sum_of_numbers(num))

# Functionn Practice

# def last_character(s):
#     return s[-1]

# print(last_character("Abrar"))

# def reverse_str(s):
#     return s[::-1]

# print(reverse_str("Amir"))

# def odd_even(n):
#     if n % 2 == 0:
#         return 'even'
#     return 'odd'

# for i in range(10):
#     print(odd_even(int(input("Enter a number: "))))

# print(odd_even(int(input("Enter a number: "))))

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False

# def is_even(n):
#     return n % 2 == 0

# print(is_even(3))

# def is_odd(n):
#     return n % 2 != 0

# print(is_odd(3))

# def greater(a, b):
#     if a > b:
#         return a
#     return b

# print(greater(1, 2))

# def greatest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     return c

# print(greatest(1, 2, 3))

# Principles -

# Kiss -> Keep it simple stupid
# Dry -> Don't Repeat Yourself

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))

# Default Paramaters

# name = "Amir"
# age = 27

# # 1. Worst
# print("My name is " + name + " and my age is " + str(age))

# # 2. format
# print("My name is {} and my age is {}".format(name, age))

# # 3. f-string
# print(f"My name is {name} and my age is {age}")

# def user_info(first_name='Unknown', last_name='Unknown'):
#     return f'My name is {first_name} {last_name}'

# print(user_info("Anshul", "Garg"))

# Variable Scope

# x = 5

# def func_1():
#     x = 7
#     return x

# print(func_1())
# print(x)

# def func_2():
#     global x
#     x = 7
#     return x

# print(func_2())
# print(x)
