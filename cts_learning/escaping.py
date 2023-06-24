### for escap sequince ###
# mystory = 'He dosen\'t like to eat \"cheese\"'
# mystory = "He doesn\'t like to eat \"cheese\""
# print(mystory)
# print(mystory)

### with help of escap sequince we saprate the line of string ###

# mystory = 'He dosen\'t like to eat the \"cheese!\"\nBut like to eat eggs.'
# print(mystory)

### how can print a file/xyz path ###

# filepath = 'c:\\2071499\desktop\\training.txt'
# print(filepath)


# filepath = "[c:\\2071499\desktop\\training.txt]"
# print(filepath)
# print(type(filepath))


################### put two string together that is called concatenation #################

# mystory = 'He dosen\'t like to eat the \"cheese!\"\nBut like to eat eggs.' + 'hello'
# #print(mystory)

# ## how can print a file/xyz path ###

# filepath = 'c:\\2071499\desktop\\training.txt'
# #print(filepath)

# print(mystory + filepath)

########## if require some syntax for print 2-3 times like that ################

# multiple_times_print = (4 * "Amir" + "\nthe last")
# print(multiple_times_print)

##### if your value will change in every action then will in that you can satisfy by .format syntax ######
 
# age = 21
# hight = 5.5
# print("My age is !!{}!! and hight is !!{}!!".format(age, hight))


"""
name = "Julie"

age = "42"

sentance = (f'Hi my name is {name} and i am {age} years old')
print(sentance)
"""
#print("Hi my name is {} and i am {} years old".format(name, age)) 
#print("Hi my name is {} and i am {} years old".format(sentance))


# name=input()
# age=input()

# message=f'{name} is {age} years old'
# print (message )

############### for replace synatx ###################

# Bob = ("Hi my name is Bob '.' " * 3)
# Bob = Bob.replace("Bob", "Amir")
# #Bob = Bob.split()
# print(Bob)

################### for get output from tuppl to list ################

# x = "My name is Mohammad Amir".split()
# print(x)

####### Capitalize all the letters in tdfw and replace the word WHAT with CHEESE,,,, Print out the result! ############

# tdfw = "turn down for what"
# tdfw = tdfw.replace("what", "cheese")
# print(tdfw.upper())

x = "Hello World"
print(x[6:])