"""indentation example"""
# if 5 > 2:
#     print("five is greater then two")

"""indention error syntex"""
# if 5 > 2: 
# print("Five is greater than two!")  #IndentationError: expected an indented block after 'if' statement on line 45
# if 5 > 2: 
#     print("Five is greater than two!")

# if 5 > 2: 
#  print("Five is greater than two!") 
# print("Five is greater than two!")

"""example of variable"""
# x = 4 # x is of type int 
# x = "Sally" # x is now of type str 
# print(x)

"""randome number module in float, integer """

# import random
# winning_number = random.randrange(1,100)
# # guess = 1
# # number = int(input("guess a number between 1 and 100 : "))
# print(winning_number)

# import random 
# print(random.randrange(1, 10))

"""define python variable"""

# x, y, z = "Cherry", "Banana", "Orange"
# print(x)
# print(y)
# print(z)

""" define one variable to multiple value"""
# x = y = z = "Apple"
# print(x)
# print(y)
# print(z)

"""define unpack collection variable list"""
##Unpack a list

# fruits = ["apple", "apple", "banana", "cherry"]
# # x, y, z = fruits
# print(fruits.count("apple"))
# print(y)
# print(z)

""" + opreator"""
# x = "python is awesome"
# y = "its a programing"
# z = "simple application"
# print(x+y+z)

# x = int(5) 
# y = "John" 
# print(x,y)

"""
This is global function
"""
# from re import X

# c = "Delhi"
# z = "Allahabad."
# b = "Noida."
# def myfunc():
#     print("I am from " + z, "Now leving in " + c, "for attend my classes in " + b)
# myfunc()    

# x = "awesome" #inside the function Global keyword
# def myfunc(): 
#     #global  x
#     x = "fantastic" 
#     print("Python is " + x)
# myfunc()
# print("Python is " + x)

#z = 200 # Global Variable
# def myfunc(n):
#     z = 5
#     g = 8
#     z=z + 2
#     print(z,g)
#     print(n, "I have printed")
# myfunc("This is me")
#print(z) 

"""global with def function"""
#l = 10
# def func(n):
#     #l = 20
#     #m = 8
#     global l
#     l = 4
#     m = 1
#     l=l + 45
#     print(l,m)
#     print(n, "I have printed")
# func("This is me")
# print(l)  
# 
# d = "Agra"
# def function():
#     c = "collage"
#     print(c)
# function()
# print(d)      

"""integer number types"""

# x = 1 #int
# y = 2.8 #float
# z = 1j # complex
# print((x),type(x))
# print((y),type(y))
# print((z),type(z))
"""float number types"""
# x = 1.10
# y = 1.0
# z = -35.59
# print(type(x))
# print(type(y))
# print(type(z))

# x = 35e3 
# y = 12E4 
# z = -87.7e100 
# print(type(x)) 
# print(type(y)) 
# print(type(z))

"""float number types"""

# x = 3+5j 
# y = 5j 
# z = -5j
# print(type(x)) 
# print(type(y)) 
# print(type(z))


# x = 1 # int 
# y = 2.8 # float 
# z = 1j # complex 
# #convert from int to float: 
# a = float(x) #convert from float to int: 
# b = int(y) #convert from int to complex: 
# c = complex(x) 
# print(a) 
# print(b) 
# print(c)

"""this is define the dictionary"""
# dict = {}
# dict = {"Amir":"9648634083", "Zaid":"9506969378", "Fahad" :{"S":"School", "Noon":"Lunch", "Night":"Dinner"}}
# print(dict["Fahad"])
# #print(dict["Zaid"])
# #print(type(dict))

# x = 500j
# y = int(x)
# print(y)

"""Kilo metter define range syntex"""
# x = (100)
# print("KM",range(x))

# x = len("My name is mohammad amir siddique")
# p = len("My collage name is CSJM kanpur")
# KM = (100)  # this is define the kilomitter
# print(x,p)
# print("KM",range(KM))

""" set syntex"""
# x = set(("amir", "zaid", "sarjeel")) # value will take dynamically in output
# print(x)
# print(type(x))
# # y = set((1,2,3))
# # print(x,y)
"""frozenset syntex"""
# x = frozenset(("apple", "banana", "cherry"))
# print(x)

# vowels = {'a','e','i','o','u'}
# froz = frozenset(vowels)
# print(froz)

"""boolean syntax"""
"""
Need to aske with vikas for true or false logic
"""
# list1 = [5, 7, 3]    ## this is also working syntax for true or false
# print(30 in list1)
# if 30 in list1:
#     print("Yes its in the list1")

# age1 = 17 ## this is working syntax
# age2 = 21
# age3 = int(input())
# if age3>age2:
#     print("Greater")
# elif age3==age2:
#     print("Equal")
# else:
#     print("Lesser")

""" bytes syntax """
# l = [10,20,30,40]
# b = bytes(l)
# print(l[3])

"""random sytax"""
# import random
# number = (random.randrange(1,9))
# #number = int(input("enter the numbers "))
# print(number)

"""for check python version"""
import sys
import this 
# print("python version")
# print(sys.version)

"""multiline string"""
# a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""" 
# print(a)

# a = "Hello, World!" # for print a particular element from a value 
# print(a[1])
"""loop strings"""
# d = input("enter your name ")
# for z in "school":
#     print(d,z)

"""len function"""
# a = "My first collage name is allahabad!"
# print(len(a))

"""check string syntax"""  #need to ask with vinay
# number = ("13, 14, 15, 16, 17")
# if "19" in number:
#     print("Yes, this number is available")
# else:
#     print("No, number is not available")
#print("17" in number)

"""need to ask with vikas"""
# list = (2, 4, 6, 8, 10)
# number = input("please enter the number ")
# if "list" in number:
#     print("Yes, this is in list")
# else:
#     print("No, not present in list")

""" print first name and last name"""
# name0 = str(input("enter the first name "))
# name1 = str(input("enter your second name "))
# # print(name[::-1])
# print(name0, name1)

# fname = input("enter your first name")
# lname = input("enter your second name ")
# print(fname + " " + lname)
""" Slicing string/  syntax"""
# b = "Hello, World!" 
# #print(b[2::5])
# #print(b[:5])
# #print(b[2:])
# print(b[-5])
# print(b[-5:-2])
"""upper syntax"""
# a = "Hello, World!" 
# print(a.upper())
"""lower syntax"""
# a = "Hello, World!" 
# print(a.lower())

"""remove white space syntax"""
# a = "            Hello, World!            " 
# print(a.strip())

"""date and time syntax"""
# from datetime import datetime
# # datetime object containing current date and time
# now = datetime.now()
# print("now =", now)
# #dd/mm/yy H:M:S
# dt_string = now.strftime("%d/%m/%y %H:%M:%S")
# print("date and time =", dt_string)
# # today = date.today()
# # print("today's date:", today)
"""replace syntax"""
# a = "Hello, World!" 
# print(a.replace("H", "J"))

# a = "Hello, World!" 
# print(a.split(",")) # returns ['Hello', ' World!']

"""split syntax"""
# name = "Mohammad Amir, Siddique"
# s = "S/O - Atiq Ahmad"
# z = name + " " + s
# print(z.split(","))
"""list syntax"""
# name = ["amir", "zaid", "abrar"]
# name[0] = "fahad"
# print(name)

""" set syntax"""
# name = {"amir", "zaid", "abrar"}
# name.update(["fahad"])
# print(name)
# print(name.replace("amir", "fahad"))
""" format string"""
# age = 36 
# txt = "My name is John, I am {}" 
# print(txt.format(age))
"""format placed holder syntax"""
# Paint = 3
# TShirt = 3
# itemno = "Paint 567", "TShirt 660"
# price_total = 50
# myorder = "I want paint {1} and TShirt {3} pieces of total item {2} for {0} dollars."
# print(myorder.format(Paint, TShirt, itemno, price_total))
"""escape syntax"""
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

"""booleans syntax"""
# b = ' '
# print(bool(b))

# school = ('Amir', 'Yasir', 'Abrar')  ## need to check with trainer true or false (when i give any logic its not coming proper value, want here put user value need to comes output)
# school = input("enter your name ")
# print("Sumit" in school)
# if 'Amir' in school:
#     print("Yes its in the school")
# else:
#     print("Not in School")

# def myFunction(): 
#     return False
# if myFunction(): 
#     print("YES!") 
# else: 
#     print("NO!")

# x = int(12) 
# print(isinstance(x, int))

# class myclass(): 
#     def __len__(self):
#         return 0 

# myobj = myclass() 
# print(bool(myobj))

# def myfuc():
#     return 1
# if myfuc():
#     print("Yes")
# else:
#     print("No")

# x = "name"
# print(isinstance(x,str))

""" and , or, not syntax"""
# x = "true"
# y = "true"
# print("x and y is ", x and y)
# print("x or y is", x or y)
# print("not x is", x)

# x = "Hello World"
# y = {1:'a',2:'b'}
# #output: True
# print('H' in x)

# #output: True
# print('Hello' not in x)

# # output: True
# print(1 in y)

# # output: False
# print('a' in y)

"""List syntax"""

# mylist = ["1","2","3","4","2"]
# thislist = ["apple", "banana", "cherry"] 
# print(mylist + thislist)

# x = list(("apple", "banana", "cherry"))
# print(x)

# b = ["apple", "banana", "cherry"]
# b.extend("mango")
# #b.insert(2,"school")
# #b.pop(1)
# print(b)

"""date and time syntax"""
# from datetime import date
# # calling the today
# # function of date class
# today = date.today()
# print("Today's date is", today)

# from datetime import datetime
# now = datetime.now()
# print(now)

"""set syntax to date"""
# x = (2,3,4,5)
# x.insert(1,"10")
# print(x)

# b = ("apple", "apple", "banana", "cherry")
# #b.extend("mango")
# #b.insert(2,"school")
# #b.pop(1)
# print(b)

# thisdict = { "brand": "Ford", "brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020 } 
# thisdict.
# print(thisdict)

# thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 }
# x = thisdict["model"]
# print(thisdict)

# car = { "brand": "Ford", "model": "Mustang", "year": 1964 } 
# x = car.keys() 
# print(x) #before the change 
# car["color"] = "white" 
# print(x) #after the change

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] 
# print(thislist[-4:-1])
# from time import datetime 
# current_time = datetime.now(timezone(zone))
# print(current_time)


# print("This is a guessing game")
# import random
# random_number = random.randrange(1,10)
# guess = int(input('What could be the number?'))
# correct = False
# print(random_number)
# while not correct:
#     if guess==random_number:
#         print('I got it')
#         correct = True
#     elif guess>random_number:
#         print("Too high")
#         break
#     elif guess<random_number:
#         print("Too low")
#         break
#     else:
#         print("Try something else")

"""list syntax"""
#fruits = ["A","B","C","D"]
# fruits = ["This is test document"]
# newlist = ['hello' for x in fruits]
# print(newlist)

"""calendar syntax"""
# import calendar 
# y = int(input("enter a year "))
# m = int(input("enter a month "))
# print(calendar.month(y,m))

# from datetime import date
# y = date.today()
# print("Current year:", y.year)
# print("Current month:", y.month)


# # importing date class from datetime module
# from datetime import date
  
# # creating the date object of today's date
# todays_date = date.today()
  
# # printing todays date
# print("Current date: ", todays_date)
  
# # fetching the current year, month and day of today
# print("Current year:", todays_date.year)
# print("Current month:", todays_date.month)
# print("Current day:", todays_date.day)

# import calendar
# year = 2022
# #month = 12
# print(calendar.calendar(year))

# import datetime
# x = datetime.datetime.now()
# print(x)

# import datetime
# x = datetime.datetime.today()
# print(x)

"""set function"""

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3} 
# set3 = {"Google", "Microsoft", "Amazon"}
# set4 = set1.union(set2, set3) 
# print(set4)

# set1 = {"Software", "Hardware", "Cloud", "Server"}
# set2 = {100, 200, 300, 400}
# set3 = {"USA", "UK", "India", "London"}
# set1.update(set2, set3)
# print(set1)

# thisset = {"apple", "banana", "mango"}
# set1 = {200, 400, 600, 800}
# thisset.discard("banana")
# thisset.update(set1)
# print(thisset)

# thisset = {"apple", "banana", "cherry"} 
# set1 = {"Microsoft", "Google", "Amazon"}
# set2 = {200, 400, 600, 800}
# b = set1.pop()
# c = set2.pop()
# x = thisset.pop() 
# y = thisset.pop()
# z = thisset.pop()
# # print(z)
# # print(y)
# # print(x) 
# thisset.update(set1, set2)
# print(b)
# print(c)
# print(thisset, x, y, z)

# thisset = {"apple", "banana", "cherry"} ############################################# need to work from here page number 90
# set1 = {"Amir in the set"}
# set2 = set1.pop()
# thisset.clear() 
# thisset.update(set1)
# print(thisset, set1)

# x = {"apple", "banana", "cherry"} 
# y = {"google", "microsoft", "apple"} 
# x.symmetric_difference_update(y) 
# print(x)

new_tuple = ()     ################# need to ask with vikash
y = list((new_tuple))
# new_code = tuple(y)
for i in range(20):
    if(i%2 == 0):
        y.append(i)
print(y)        


# atuple = (123, 'xyz', 'zara', 'abc')
# alist = list(atuple)
# print("List element:", alist)