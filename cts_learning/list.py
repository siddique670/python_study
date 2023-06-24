## to add the value in a list variable

# animals = ['man', 'bear', 'cow']
# animals.append('bull')
# print(animals)


## called the value in negative

# animals = ['humman', 'owl', 'cow']
# print(animals[0])
# print(animals[1])
# print(animals[2])
# print(animals[-1])
# print(animals)

### to add a multiple iteam in a single list in a once

# animals = ['man', 'bear', 'cow']
# animals.extend(['duck', 'bull'])
# print(animals)

### here number is represent the indexing where you want to put the value

# animals = ['man', 'bear', 'cow']
# animals.insert(0, 'horse')
# print(animals)


# animals = ['man', 'bear', 'cow']
# animals.insert(2, 'horse')
# print(animals)

############## Slices ##############


# animals = ['man', 'bear', 'cow', 'duck', 'horse']
# some_animals = animals[1:4]
# print('some animals:{}'.format(some_animals))

# first_two_animals = animals[0:2]
# print('first two animals:{}'.format(first_two_animals))

# first_two_again = animals[:2]
# print('first two again{}'.format(first_two_animals))

# print(animals[-2:]) 

# animals = 'Mohammd Amir'[2:9]
# print(animals)

########### Exception Handdel ##########

# animals = ['man', 'cow', 'bull', 'cat']
# cat_animals = animals.index('cat')    """ with this line we get the error """
# cat_index = animals.index('cat')
# print(cat_index)


# animals = ['man', 'bear', 'cow']
# try:
#     cat_index = animals.index('cat')
# except:
#     cat_index = 'No cats found'
# print(cat_index)


############ Loops ############## Looping through a list

# list_name = 'item_variable'    ############### need to check this code with teacher#############
# def my_fuc(list_name):
#     for item_variable in list_name:
#         item_variable = ['man']
#         item_variable = ['cow']
#         item_variable = ['bull']
# my_fuc()        
# print(list_name)

########### upper case looping ###########

# animals = ['man', 'bear', 'cow']
# for animal in animals:
#     print(animal.upper())

# animals = ['man', 'bear', 'cow', 'duck', 'horse']
# index = 0
# while index < len(animals):
#     print(animals[index])
#     index += 1

### to sorted the list value in alfhabaticall###

# animals = ['man', 'bear', 'cow', 'duck', 'horse']
# sorted_animals = sorted(animals)
# print(sorted_animals)


# animals = ['man', 'bear', 'cow', 'duck', 'horse']
# sorted_animals = sorted(animals)
# #print('animals list:{}'.format(animals))
# # print('animals{}'.format(animals))
# # print('sorted animals list:{}'.format(sorted_animals))
# #animals.sort()
# print('animals after sort method:{}'.format(animals))

##### to concaniate the multiple list value in single value ###

# animals = ['man', 'bear', 'cow']
# more_animals = ['duck', 'horse']
# all_animals = animals + more_animals
# print(all_animals)

###### to check tha total of value with the len function and range function #####

# animals = ['man','duck', 'horse']
# for number in range(1, 3):
#     print(len(animals))
# animals.append('cow')
# print(len(animals))
# #print(range(animals))

# number = 10
# for number in range(1, 10, 2):
#     print(number)

# animals = ['man', 'bear', 'cow', 'duck', 'horse']
# for number in range(0, len(animals), 2):
#     print(animals[number])



# favgame = ["Mario Bros 3", "Earthbound", "Pilotwings"]
# del(favgame[len(favgame)-1])
# print(favgame)

# t = ["ab","de","fg","jk"]

# def append(tup, value):
#     return (tup+ value, value + tup)
# equal = append(tup= t, value= t )
# print(equal)


# games = set(["Mario Bros 3", "Earthbound", "Pilotwings", "Mario Party"])
# games.discard("Pilotwings")
# print(games)


## Create a set called unique that holds all the unique numbers from the list called numbers.

# numbers = [3, 2, 2, 4, 5, 5, 2, 4, 9, 3, 10, 10, 1, 5, 2, 10, 1, 9, 2]

# numbers = [3, 2, 2, 4, 5, 5, 2, 4, 9, 3, 10, 10, 1, 5, 2, 10, 1, 9, 2]
# #unique = [x for x in numbers if x not in numbers and numbers.apppend(x)]
# unique = set(numbers)
# print(unique)    """ correct answaer """"
1
# def get_unique_numbers(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)
#     for number in unique_numbers:
#         list_of_unique_numbers.append(number)
#     return list_of_unique_numbers
# print(get_unique_numbers(numbers))



# numbers = [1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]
# def get_unique_numbers(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)
#     for number in unique_numbers:
#         list_of_unique_numbers.append(number)
#     return list_of_unique_numbers
# print(get_unique_numbers(numbers))


# Question :- We're back at it again with the shoes list. I have provided you with the shoes list from the last exercise.

# In this exercise, I want you to make a function called addtofront, which will take in two parameters, a list and a value to add to the beginning of that list.

# Once you have made your function, add this line of code to your exercise:

# addtofront(shoes, "White Vans")

# Solution :- 
# shoes = ["Spizikes", "Air Force 1", "Curry 2", "Melo 5"]

# def addtofront(shoe_list, front_shoe):
#     shoe_list.insert(0, front_shoe)

# addtofront(shoes, "White Vans")
# print(shoes)

# shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5")

# def appendtotuple(thetuple, value):
#     tuple1 = thetuple
#     tuple2 = value
#     tuple3 = tuple1+(value,)
#     return tuple3
# print(appendtotuple(shoes,shoes))

# import datetime 

# x = datetime.now()
# print(x)

# from datetime import datetime
  
# time = datetime.now()
# print(time)


numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

odds = {num for num in numbers if num %2 == 1}
print(odds)