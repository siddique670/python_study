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
# name = input("enter your name ")
# print("Amir" in school)
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

# sh echo 'Print Output'

# a = "Hello, World!" 
# print(a.split(","))

"""duplicate syntax print"""

# x = {"apple", "banana", "cherry"} 
# y = {"google", "banana", "apple"} 
# x.intersection_update(y) 
# print(x)

# set1 = {"a", "b" , "c"} 
# set2 = {1, 2, 3} 
# set3 = set1.union(set2) 
# print(set3)

# set1 = {"a", "b" , "c"} 
# set2 = {1, 2, 3} 
# set1.update(set2) 
# print(set1)

# x = {"apple", "banana", "cherry"} 
# y = {"google", "microsoft", "apple"} 
# x.symmetric_difference_update(y) 
# print(x)

# x = {"apple", "banana", "cherry"} 
# y = {"google", "microsoft", "apple"} 
# z = x.intersection(y) 
# print(z)

# x = {"apple", "banana", "cherry"} 
# y = {"google", "microsoft", "apple"} 
# z = x.symmetric_difference(y)
# print(z)

"""Dictionary syntax"""

# thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 } 
# print(thisdict)

# listdict = {"School": "Class", "Univercity": "Lecture", "Year": 2014}
# print(listdict["School"])

"""Duplicate values will overwrite existing values:"""

# thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020 } ############# how to come 3 lenth
# print(len(thisdict))

"""String, int, boolean, and list data types"""

# thisdict = { "brand": "Ford", "electric": False, "year": 1964, "colors": ["red", "white", "blue"]}
# print(thisdict["colors"])

"""define the data type"""

# thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 } 
# print(type(thisdict))


# thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 } 
# x = thisdict["model"]
# x = thisdict.get("model")
# print(x)

# car = { "brand": "Ford", "model": "Mustang", "year": 1964 }
# x = car.keys()
# print(x)
# car["color"] = "white"
# print(car)

# car = { "brand": "Ford", "model": "Mustang","year": 1964, "Collage": "Classes" } 
# x = car.values() 
# print(x) #before the change car["year"] = 2020 print(x) #after the change

# car = { "brand": "Ford", "model": "Mustang", "year": 1964 } 
# x = car.values() 
# print(x) #before the change 
# car["color"] = "red" 
# print(x) #after the change

# car = { "brand": "Ford", "model": "Mustang", "year": 1964 } 
# z = car.items()
# y = car.values()
# car["color"] = "black"
# car["year"] = 2020 
# x = car.get("brand")
# print(type(car)) 
# print(len(car))
# print(x)
# print(y)
# print(z) #before the change 
# print(x) #after the change

car = { "brand": "Ford", "model": "Mustang", "year": 1964 } 
x = car.items() 
print(x) #before the change car["color"] = "red" print(x) #after the change