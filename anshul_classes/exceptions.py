# Introduction of Errors -

# Syntax Error
# Indentation Error
# Name Error
# Type Error
# Index Error
# Value Error
# Attribute Error
# Key Error ..etc

# Raise Error -

# def add(a, b):
#     return a + b

# def add(a, b):
#     if type(a) and type(b) != int:
#         raise TypeError('Only integers are allowed.')
#     return a + b

# print(add(2, 3))
# print(add("2", "3"))

# Exception Handling

# print(2 / 0)

# try:
#     age = int(input("Enter your age : "))

# except ValueError as e:
#     print("Only integers are allowed.")

# except Exception as e:
#     print(e)

# else:
#     print(age)

# finally:
#     print("Exception handling..")
