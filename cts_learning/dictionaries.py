## hold key-value pairs called ites.

from operator import contains


# contacts = {'Amir': '123-4567', 'Abrar': '123-457'}
# amir_phone = contacts['Amir']
# abara_pjone = contacts['Abrar']
# print('Dail {} to call Amir.'.format(amir_phone))
# print('Dail {} to call Abrar.'.format(abara_pjone))

#### to add the anothe dict value in a single dict#######

# contacts = {'Amir': '123-4567', 'Abrar': '123-457'}
# contacts['Tony'] = '123-4567'
# print(contacts)

####### to delete the single value from dict #####

# contacts = {'Amir': '123-4567', 'Abrar': '123-457'}
# contacts['Tony'] = '123-4567'
# del contacts['Amir']
# print(contacts)

#### some value in string and some value have in int ###

# contacts = {'Amir': ['123-4567', '123-457'],'Tony': '123-4567'}
# print('Amir:')
# print(contacts['Amir'])
# print('Carl:')
# print(contacts['Tony'])

### print the only value from the key -dict ###### 
# contacts = {'Amir': ['123-4567', '123-457'],'Tony': '123-4567'}
# for number in contacts['Amir']:
#     print('Phone:{}'.format(number))

##### if value of the key is available in dict then thru is return ######

# contacts = {'Amir': ['123-4567', '123-457'],'Tony': '123-4567'}
# if 'Amir' in contacts.keys():
#     print("Amir phone number is:")
#     print(contacts['Amir'][0])

# if 'Tony' in contacts.keys():
#     print("Tony phone number is:")
#     print(contacts['Tony'][0])

# contacts = {'Amir': ['123-4567', '123-457'],'Tony': '123-4567'}
# print('123-4567' in contacts.values())

# contacts = {'Amir': ['123-4567', '123-457'],'Tony': '123-4567'}
# for contact in contacts:
#     print('The number for {0} is {1}.'.format(contact, contacts[contact]))

#######   office error code   #########

# contact = "{'Amir':{'phone': '123-4567', 'email': 'amir@xyz.com'}, 'Tony':{'phone': '123-4567', 'email': 'tony@xyz.com'}"
# for contact in contact:
#     print("{}'s contacts info:".format(contains))
#     print(contact[contact]['phone'])
#     print(contact[contact]['email'])


# dogs = {"Dido":8, "Sean":8, "Jane":8, "Fido":19, 8:"Hello"}
# print(dogs)

# Question """I have provided you with two lists. words and definitions

#Create a dictionary called cooldictionary where you use words for keys and definitions for values"""

# words = ["PoGo","Spange","Lie-Fi"]
# definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"] 
# cooldictionary = {}
# for word in words:
#     for definition in definitions:
#         cooldictionary[word] = definition
#         definitions.remove(definition)
#         break
# print(cooldictionary)

#############    for add/delet value in dictionaries value and pair      ################
# dogs = {"Dido":8, "Sean":8, "Jane":8, "Fido":19, 8:"Hello"}
# dogs["Delhi"] = 12
# del(dogs["Dido"])
# print(dogs)

######### for print the key value and type  #############
# dogs = {"Dido":8, "Sean":8, "Jane":8, "Fido":19, 8:"Hello"}
# print(dogs.keys())
# print(type(dogs.keys()))

############ for print key value as in list ############
# dogs = {"Dido":8, "Sean":8, "Jane":8, "Fido":19, 8:"Hello"}
# for name in dogs.keys():
#     print(name)
# for name in dogs.values():
#     print(name)
# for name in dogs.items():   #"""output get in tuppels"""
#     print(name)  
# print(type(dogs.keys()))  
# print(type(dogs.items()))  


# dogs = {"Fido":8, "Sean":8, "Jane":8, "Fido":19}
# names = dogs.keys()
# listnames = list(dogs.keys())
# print(names)
# print(listnames)
# del(dogs["Jane"])
# print(names)
# print(listnames)


# I have given you a list called dabools that has 500 booleans in it. Create a dictionary called count that has two entries. 
# One where True is the key and the number of times that True shows up in dabools is the value. 
# And another where False is the key and the number of times that False shows up in dabools is the valu

dabools = [False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, True, True, 
False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, 
False, False, True, True, False, False, True, True, True, True, True, False, True, True, False, True, False, False, True, False, 
False, False, False, True, True, False, False, True, True, True, False, True, True, False, False, False, False, True, True, False, 
True, True, False, True, True, True, False, False, False, True, True, False, True, False, True, False, True, True, True, False, 
True, False, False, True, True, False, True, False, False, True, False, True, False, True, False, True, True, True, True, False, 
False, True, True, False, False, False, False, True, True, True, False, False, True, True, True, True, True, False, True, True, 
False, False, True, True, False, False, True, True, True, True, True, False, False, True, True, False, False, True, True, False, 
False, False, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, True, True, False, 
False, True, True, True, True, True, False, True, True, True, True, True, False, False, True, False, False, False, True, True, 
True, False, True, False, False, True, False, False, True, True, False, False, False, False, True, False, False, True, True, 
False, True, True, False, False, True, False, True, True, False, True, False, True, False, True, False, False, True, False, 
True, False, False, False, True, True, False, False, False, True, True, False, False, True, True, True, True, True, False, 
True, True, True, True, False, False, True, False, True, True, True, True, True, False, False, False, True, True, False, 
True, True, True, False, False, True, True, False, True, True, True, True, False, True, True, False, False, False, True, 
True, True, True, True, False, False, False, True, False, False, False, True, False, True, True, True, True, False, False, 
False, True, False, False, False, False, True, True, False, True, False, False, True, False, False, False, True, True, True, 
False, False, True, True, False, False, True, True, False, False, True, False, True, False, True, True, True, False, True, True, 
True, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, True, False, True, False, 
False, True, True, False, True, False, False, True, True, True, False, True, True, True, False, False, False, True, False, True, 
True, False, True, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, True, True, 
False, False, True, True, True, False, False, True, False, True, True, True, True, False, False, True, True, False, False, True, 
True, False, True, False, True, True, True, True, True, False, False, False, True, False, False, True, False, False, True, True, 
False, False, False, False, False, False, True, False, True, False, False, True, True, False, True, True, True, False, True, 
True, False, False, True, False, False, True, True, False, True, False, True, False, False, True, False, True, True, False, 
False, True, True, False, False, True, False, False, False, False, True, False]

# count = {dabools}
# for count in dabools():
#     print(sum(count))

# count = {
#     True: dabools.count(True),
#     False: dabools.count(False),
# }
# print(count)

# counts = {'Trues':sum(dabools), 'Falses':len(dabools)-sum(dabools)}
# print(counts)

