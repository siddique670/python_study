# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.amazon.co.in")
# print("Application title is ",driver.title)
# print("Application url is ",driver.current_url)
# driver.quit()

# once again start same python class
# print("this is \\\\ double backslash")
# print("this are /\/\/\/\/\/\/\/\ mountain ")
# print("he is \t awesome ")
# print("\\\" \\n \\t \\\'")
# print (round(2*0.4,4))

# from multiprocessing.sharedctypes import Value


# name = input("enter your name ")
# print("hello " + name)
# age = input("What is your age")
# print("your age is " + age )

# num = input("enter your first number :")
# num = input("enter your second number :")
# num = input("enter your third number :")
# num, num, num = input("enter three numbers comma separated: ").split(",")
# #print(int(num1) + int(num2) + int(num3)) / 3
# print(f"average of three number : {(int(num) + int(num) + int(num)) / 3}")

# from audioop import reverse
# from curses import echo
# from datetime import datetime
# from itertools import count
# from unicodedata import name

# fruit = input("enter favorate fruit name")
# print("Excellent " + fruit)

# number_one = int(input("enter first number"))
# number_two = int(input("enter second number"))
# total = number_one + number_two
# print("total is " + str(total))

# name, age = "Amir", "26"
# print("Hello " + name + " Your age is " + age)

# name, age = input("enter your name and age ").split(",")
# print(name)
# print(age)

# name = "Amir"
# age = 26
# print("hello " + name + "your age is " + str(age))
# print("hello {} your age is {} ".format(name, age + 2))

# number1 = int(input("enter first number"))
# number2 = int(input("enter second number"))
# number3 = int(input("enter third number"))
# # (int(number1) + int(number2) + int(number3)) / 3
# print (f"average of three numbers : {(int(number1) + int(number2) + int(number3)) / 3}")

#string indexing
# latterseq = "MOHAMMAD"
# # positions(index number)
# M = 0
# O = 1
# H = 2
# A = 3
# M = 4
# M = 5
# D = 6
# print(latterseq[::-1])

# name = input("enter your name")
# reverse = name[-1::-1]
# print(f"reverse of your name is {reverse}")

# string methods part one

# name = "Mohammad Siddique"
# # 1. len() function
# print(len(name))

# # 2. lower() method
# print(name.lower())

# # 3. upper() method
# print(name.upper())

# # 4. title() method
# print(name.title())

# # 5. count() method
# print(name.count("m"))

# name, char = input("enter comma separated name and chaacter : ").split(",")
# print(f"lenght of your name is {len(name)}")
# #print(f"character count : {name.lower().count(char.lower())}")

# print(f"character count : {name.strip().lower().count(char.strip().lower())}")

# string = "She is beautiful and she is good dancer"
# # print(string.replace(" ", "_"))
# is_pos2 = string.find("is")
# print(is_pos2)

# name = input("enter your name : ")
# print(name.center(len(name)+2, "@"))

# name = "Mohammad " 
# name = name + "Amir"
# age = 26
# age = age + 1 
# print(name)
# print(age)

# age = int(input("enter your age "))
# if age >= 14:
#     print("Your age should be under 14")
#     print("your are above 14")
# else:
#     print("Grate!!! Your age is matches")

# winning_number = 27
# user_input = int(input("guess a number b/w 1 and 100 : "))

# if user_input == winning_number:
#     print("You Win !!!")
# else:
#     if user_input < winning_number:
#         print("too low")
#     else:
#         print("too high")    

# name = "Mango"
# age = 26
# if name=="Mang" or age==29:
#     print("Condition True")
# else:
#     print("Condition False")

# name = input("enter your name please : ")
# age = int(input("enter your age please : "))
# if age >= 14 and (name[0]=="A" or name[0] == "A"):
#     print("You can watch Coco movie")
# else:
#     print("You can't watch the Coco movie")

# show ticket pricing
# 1 to 3 (Free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

# age = int(input("please enter your age "))

# if 0<age<=3:
#     print("Ticket price : free")
# elif 3<age<=10:
#     print("Ticket price : 150")
# elif 10<age<=60:
#     print("Ticket price : 250")
# else:
#     print("Ticket price : 200")

# name = input("enter your name Mohammad ")
# if "M" in "Mohammad":
#     print("name")

# datetime = ("DD/MM/YYYY")
# print(datetime)

# check empty or not
# important
# name = ""
# if name: # true if string is not empty
#     print("string is not empty")
# else:
#     print("string is empty")

# name = input("enter your name : ")
# if name: # true if string is not empty
#     print(f"your name is {name}")
# else:
#     print("you didn't type anything")

# i = 1
# while i<=10:
#     print(f"hello bro {i}")
#     i = i + 1

# n = int(input("enter a number "))
# total = 0
# i = 1
# while i <= n:
#     total += i
#     i += 1
# print(total)

# import numbers


# numbers = input("enter a number ")
# # "1256" # length = 4 , last index = 3
# # int(number[i])

# total = 0
# i = 0
# while i < len(numbers):
#     total += int(numbers[i])
#     i += 1
# print(total)

# from itertools import count


# name = input("enter your name ")
# #Mohammad Amir
# temp_var = ""
# i = 0
# while i < len(name):
#     if name[i] not in temp_var:
#         temp_var += name[i]
#     print(f"{name[i]} : {name.count(name[i])}")
#     i += 1

# from re import I

# for i in range(1, 10):
#     print(f"hello world : {i}")
#     print("this is line \n ")

# n = int(input("enter the number : "))
# total = 0
# for i in range(1,n+1):
#     total += i
# print(total)

# name = input("enter your name : ")
# temp = ""
# for i in range(len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]}: {name.count(name[i])}")
#         temp += name[i]

# for i in range(1, 11):
#     if i == 4:
#         continue
#     print(i)

# import random
# winning_number = random.randint(1,100)
# guess = 1
# number = int(input("guess a number between 1 and 100 : "))
# game_over = False

# Gaming Code for loop wise operator

# while not game_over:
#     if number == winning_number:
#         print(f"you win, and you guessed this number in {guess} times ")
#         game_over = True
#     else:
#         if number < winning_number:
#             print("too low ")
#             guess += 1
#             number = int(input("guess again : "))
#         else : 
#             print("too high")
#             guess += 1
#             number = int(input("guess again : "))

# name = "Mohammad"
# for i in range(len(name)):
#     print(name[i])

# For loop operator 

# num = input("enter a number ")
# total = 0
# for i in num:
#     total += int(i)
# print(total)    

# for function operator

# def add_two(num1,num2):
#     return num1 + num2
# a = int(input("enter a number : ")) 
# b = int(input("enter a number : "))   

# total = add_two(a,b)
# print(total)

# def add_two(num1,num2):
#     return num1 + num2
# first_name = input("type your first name ")
# last_name = input("type last name ")
# print(add_two(first_name,last_name))

# return vs print

# def add_three(a,b,c):
#     print(a+b+c)
# print(add_three(5,5,5))

# functions practice

# def last_char(name):
#     return name[-1]
# print(last_char("Mohammad Amir"))

# def odd_even(num):
#     if num%2 == 0:
#         return "even"
#     return "odd"
# print(odd_even(10))  
# 
# from turtle import pen


# def is_even(num):
#     if num%2 == 0:
#           return True
#     else:
#         return False
# print(is_even(9))  
# 
# def greater(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# num1 = int(input("please enter the fisr number "))
# num2 = int(input("please enter the second number "))
# bigger = greater(num1, num2)
# print(f"{bigger} is greater")

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(greatest(10,40,20))

#fibonacci_seq(n):
# def fibonacci_seq(n):
#     a = 0 # first number , a = 1
#     b = 1 # second number , b = 1
#     if n == 1 :
#         print(a)
#     elif n == 2:
#         print(a, b) # a b, 0 1
#     else:
#         print(a,b, end = " ")
#         for i in range(n-2):
#             c = a + b # c = 1 , 2 , 3
#             a = b # a = 1 , 1 , 2
#             b = c # b = 1 , 2 , 3
#             print(b , end = " ")   
# fibonacci_seq(5) 
# 
# def user_info(first_name = 'unknown', last_name = 'unknown', age = None):
#     print(f"Your first name is {first_name}")
#     print(f"Your last name is {last_name}")
#     print(f"Your age is {age}")

# user_info('Mohammad',24)   
# 
# scope function
# x = 5 # Global Variable
# def func():
#     global x
#     x = 7 # local variable
#     return x

# print(x)
# print(func())  

# fruits1 = ["Mango", "Orange"]
# fruits2 = ["Grapes", "Apple"]
# fruites = fruits1 + fruits2
# print(fruites)
# fruits1.extend(fruits2)
# print(fruits1)
# print(fruits2)
# 
# fruits = ['mango', 'apple', 'pear', 'kiwi']
# if 'mango' in fruits:
#     print("mango is available ")
# else: 
#     print("mango is not available ")  
# 
# split method
# name, age = input("enter your name and age ").split(",")
# print(name)
# print(age) 
# 
#for loop syntex
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']
# for fruit in fruits:
#     print(fruit)
# 
#list inside the list
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# # for i in matrix:
# #     print(i)    
# print(matrix[1][2])
# 
# import numbers


# def square_list(l):
#     square = []
#     for i in l:
#         square.append(i**2)
#     return square
# numbers = list(range(1,11))
# print(square_list(numbers)) 
# 
# define a function which will take as a argument and this function 
# will retrun a reversed list

# examples [1,2,3,4] ----> [4,3,2,1]
# ['word1', 'word2'] ---> ['word2', 'word1']
# 
# note you simply do this with reverse method or [::-1]
# but try to do this with the help of append and pop method 
# from tkinter import Variable


# def reverse_list(l):
# #     return l[::-1]
# # numbers = [1,2,3,4]
# # print(reverse_list(numbers)) 

#      r_list = []
#      for i in range(len(l)):
#         popped_item = l.pop()
#         r_list.append(popped_item)
#      return r_list 
# numbers = [1,2,3,4]
# print(reverse_list(numbers))

#define a function that take list of words as argument and return list with reverse of every element in that list
# example 
#['abc', 'tuv', 'xyz'] ---> ['cba', 'vut', 'zyx]

# def reverse_elements(l):
#     elements = []
#     for i in l:
#         elements.append(i[::-1])
#     return elements
# words = ['abc', 'tuv', 'xyz']
# print(reverse_elements(words))

# # common elements finder function
# # define a functions which take 2 lists as input and return a list
# # which contains common elements of both lists

# # example
# # input ---> [1,2,5,8], [1,2,7,6]
# # output ---> [1,2]

# def common_finder(l1, l2):
#     output = []
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output
# print(common_finder([1,2,5,8], [1,2,7,6]))

# # min and max function
# numbers = [6,60,2]
# print(max(numbers))
# print(min(numbers))
# def greatest_deff(l):
#     return max(l) - min(l)
# print(greatest_deff(numbers))


# def sublist_counter(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count
# mixed = [1,2,3, [1,2], [3,4]]
# print(sublist_counter(mixed))


# from selenium import webdriver
# from selenum.webdriver.common.by import By
# from selenium.webdriver.support.ui import webDriverWait
# from selenium.webdriver.support import expected_condition as EC
# from selenium.webdriver.support.ui import Select
# from webdriver_manager.chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome(ChromeDriverManager() .install())

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


from selenium import webdriver
driver = webdriver.Chrome()