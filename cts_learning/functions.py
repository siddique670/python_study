# def say_hi(name):
#     print('Hi {}!'.format(name))
# say_hi('Jason')
# say_hi('everybody')

# def say_hi(first, last):
#     print('Hi {} {}!'.format(first, last))
# say_hi(first = 'June', last = 'Done')
# say_hi(last = 'Doe', first = 'John')


# def odd_or_even(number):
#     """Detrmine if a number is odd or even"""
#     if number % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
# odd_or_even_string = odd_or_even(7)
# print(odd_or_even_string) 
# 
#
# def is_odd(number):
#     """Determine id a number is odd"""
#     if number % 2 == 0:
#         return False
#     else:
#         return True
# print(is_odd(2)) 
# 
# 
# def get_name():
#     name = input('What is your name? ')
#     return name

# def say_name(name):
#     print('Your name is {}.'.format(name))

# def get_and_say_name():
#     """Get and display name"""
#     name = get_name()
#     say_name(name)

# get_and_say_name()   
# 
# client_path = r"C:\ProgramData\Cognizant\AutomationCenter\Scripts\eyethon_script\EyethonV2-Application\AWS_Server\eyethon\invoke.ps1"
# print(client_path)
# 
# 
# ################## Funcrion 02 ###############
# 

# def hello():
#     print("Hello World")
#     print("It smells nice outside")
# hello()  
# 

# ########  Made certificate sheet  ##########
# pointspossible = 100
# studentname = input("Student Name: ")
# def calcthegrade():    
#     percent = round(score / pointspossible, 2)
# #print("Percentage is {}".format(percent))
#     grade = "Error"

# # """
# # A - 100-90%
# # B - 89-80%
# # C - 79-70%
# # D - 69-60%
# # F - 59-0%
# # """
# #grade = "A"

#     if 1 >= percent >= 0.9:
#         grade = "A"
#     elif 0.9 > percent >= 0.8:
#         grade = "B"
#     elif 0.9 > percent >= 0.7:
#         grade = "C"
#     elif 0.9 > percent >= 0.6:
#         grade = "D"
#     else:
#         1 >= percent >= 0.5
#     grade = "F"    

# ###  Print the student name and what grade they got
#     print("{} - {}".format(studentname, grade))

# try:
#     score = int(input("Student Score: "))
#     calcthegrade()   
# except Exception:
#     print("Please provide valid number")     
        ##  score = 0  ## """this is additional syantx we can try and test """
# percent = round(score / pointspossible, 2)   ## """ this is additional syantx we can try and test """



# def love():
#     print("I love python!")
# love()

# """ below syntax is has correct"""
# def love():
#     print("I love Python!")

# def ilovepython():
#     for i in range(1):
#         print('I love Python!')
# ilovepython()


# def mablib(name, verb, noun):
#     print(name + " was " + verb + " with " + noun)
# # mablib("Zaid", "Nick", "Running")    
# mablib(noun="Zaid", name="Nikc", verb="Running")

# Create a function called firstletter that takes one string as a parameter. Then in the function, print the first letter of that string.

# def firstletter(x):
#     print(x[0])


################## missing argument, i mean error with code #####################

# def mablib(name, verb, noun):
#     print(name + " was " + verb + " with " + noun)
# # mablib("Zaid", "Nick", "Running")    
# mablib()

# def mablib(name="Zaid", verb="Eating", noun="Tobaco", *thelasttime):
#     print(name + " was " + verb + " with " + noun + "!")
#     #print(thelasttime)
# mablib("Zaid", "Nick", "Running")    
# # mablib("Zaid", "Eating", "Tobaco", 1,2,3, "from school time")



##########  Retrun function ############

# def addtwo(num1, num2):
#     total = num1 + num2
#     return total

# print(addtwo(3, 6))


# def addtwo(num1, num2):
#     total = num1 + num2
#     return total
#     print("Hello")
# thenum = addtwo(3, 6)
# print(thenum)


# def addtwo(num1, num2) -> int:
#     total = num1 + num2
#     return total
#     print("Hello")
# thenum = addtwo(3, 6)
# print(thenum)



# def printtype(num1, num2):
#     total = num1 + num2
#     return total
#     print("Hello")
# thenum = printtype(3, 6)
# print(type(thenum))


# def whattype():
#     user = ("2")
#     try:                                                
#             user = float(user)                      
#             print(type(user ** 2))
#     except ValueError:
#             print("Sorry Dave, I'm afraid I can't do that")
#             return 0.0

# whattype()


# def distance_from_zero(n):
#     if type(n) == int:
#         return abs(n)
#     elif type(n) == float:
#         return abs(n)
#     else:
#         return "Not an integer or float!"
# distance_from_zero(10)


# def printtype(num1, num2):
#     total = num1 + num2
#     return total
# thenum = printtype(3, 6)
# print(type(thenum))


# def printtype(num1, num2):
#     total = num1 + num2
#     return total
# thenum = printtype(3, 6)
# print(type(thenum))


# def printtype(var1: str, var: str, var3) -> str: 
#     return var1 + var + var3
#     return total
# thenum = printtype(7, 8)
# num = printtype(3.5, 7)
# value = printtype("3", "6")
# print(type(thenum))
# print(type(num))
# print(type(value))


# def distance_from_zero(a):
#     if type(a) == int or type(a) == float and type(a) == str:
#         print (a)
#     else:
#         print ('Not an integer or a floating point decimal!')

# distance_from_zero(type(5.5))


# def printtype(a):
#     if type(a) == int:
#         print(a) 
#     elif type(a) == float:
#         print (a)
#     else:
#         type(a) == str
#     print(a)
#         # print ('Not an integer or a floating point decimal!')
# printtype(type(5))


# def printtype(x): 
#     if isinstance(x,int):
#         return x
#     elif isinstance(x,float):
#             return x
#     else:
#         isinstance(x,str)
#         return x
#     #else: 
#     #    return None 
# print(type(printtype(5)))
# print(type(printtype(5.0)))
# print(type(printtype("5")))


# def weather(answer):
#     while answer == 'y':
#         temperature = float(input("Enter the temperature for today: "))
#         print("You have entered ", round(temperature, 2))
#         print(displayResult(temperature))
#         answer = input("Would you like to enter the temperature for today (y/n)? ")

#     print("Goodbye!")
# def displayResult(temperature):
#     if temperature >= 30:
#         return "The weather is very hot today"
#     elif temperature >= 20:
#         return "The weather is beautiful today"
#     elif temperature >= 10:
#         return "The weather is cool today"
#     else:
#         return "The weathere is very cool today"
# answer = input("Would you like to enter the temperature for today (y/n)? ")
# weather(answer)


# def printtype(x): 
#     if isinstance(x,int):
#         return "Int"
#     elif isinstance(x,float):
#             return "Float"
#     else:
#         isinstance(x,str)
#         return "String"
      
# print(printtype(5))
# print(printtype(5.0))
# print(printtype("5"))