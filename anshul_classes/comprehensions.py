# List Comprehension -

# 1. List out squares of 1 to 10

# squares = []

# for i in range(1, 11):
#     squares.append(i**2)

# print(squares)

# squares = [i**2 for i in range(1, 11)]
# print(squares)

# 2. List out negatives of 1 to 10

# negatives = [-i for i in range(1, 11)]
# print(negatives)

# 3. List of first character of each name from names list

# names = ['ABC', 'BCD', 'DEF']

# first_chars = [name[0] for name in names]
# print(first_chars)

# 4. List of reverse of each name from names list

# names = ['ABC', 'BCD', 'DEF']

# reverse_names = [name[::-1] for name in names]
# print(reverse_names)

# 5. with if statement -

# evens = [i for i in range(1, 11) if i % 2 == 0]
# print(evens)

# odds = [i for i in range(1, 11) if i % 2 != 0]
# print(odds)

# 6. with if and else statement -

# Create a list of negative odd numbers with double the even numbers

# out = [-i if i % 2 != 0 else i**2 for i in range(1, 11)]
# print(out)

# 7. [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# outer_list = []

# for i in range(1, 4):
#     inner_list = []

#     for j in range(1, 4):
#         inner_list.append(i)

#     outer_list.append(inner_list)

# print(outer_list)

# outer_list = [[] for i in range(1, 4)]
# print(outer_list)

# outer_list = [[i for i in range(1, 4)] for i in range(1, 4)]
# print(outer_list)

# 8. [[[1, 2], [1, 2]], [[1, 2], [1, 2]]]

# outer_list = []

# for i in range(1, 3):
#     inner_list_1 = []

#     for j in range(1, 3):
#         inner_list_2 = []

#         for k in range(1, 3):
#             inner_list_2.append(k)

#         inner_list_1.append(inner_list_2)

#     outer_list.append(inner_list_1)

# print(outer_list)

# outer_list = [[[k for k in range(1, 3)] for j in range(1, 3)] for i in range(1, 3)]
# print(outer_list)

# Set Comprehensions -

# evens = {i for i in range(1, 11) if i % 2 == 0}
# print(evens)

# Dictionary Comprehensions -

# evens = {i:i for i in range(1, 11) if i % 2 == 0}
# print(evens)
