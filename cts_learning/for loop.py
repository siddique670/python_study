####### Range Function #########
# for x in range(5):
#     print("I love Python!")

# for y in range(10):
#     print(y)

# for z in range(10, 20):
#     print(z)

# names = ["Amir", "Abrar", "Zaid"]
# for x in names:
#     print(x)


### Question :- I have given you a list of ints called numbers. I want you to create a set called odds that holds all the odd numbers from that list.

# numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]
 
# # iterating each number in list
# for num in numbers:
 
#     # checking condition
#     if num % 2 != 0:
#         print(num, end=" ")


########### while loops ###############

# age = 27
# while age < 50:
#     print(age)
#     age += 1


# #guess_game = input("Guess a number between 1 and 10: ")
# while guess_game != "8":
#     guess_game = input("Guess a number between 1 and 10: ")
# print("You win! ")


# x = 2 ** 10
# print(x)

# base=2
# num=1

# while base**num > 1000000000:
#    print(num)
#    num +=1

# base = 2
# power = 1
# value = 1000000000
# output = base**power
# while output <= value:
#     power+=1
#     output = base**power
#     print(output, power)
    
# print(power)

## Questions :-  2 raised to what power, is greater than 1,000,000,000? Print the answer (the answer should be an int)


# base = 2
# num = 0
# while (base**num < 1000000000):
#    num += 1
# print(num)

##### if statement with code #######

# for x in range(10):
#     print(x)
#     if x == 7:
#         continue
#     print("hey there")
# print("All done and good!")

#### else and if condition ######

# for x in range(10):
#     print(x)
#     #if x == 5:
#         #continue
#     #print("hey there")
# else:
#     print("WOW!")
# print("All is best!")

nums = [99, 20, 30, 35, 16, 49, 39, 11, 69, 48, 85, 32, 10, 47, 24, 80, 37, 21, 3, 99, 13, 11, 23, 12, 40, 50, 24, 14, 
10, 62, 21, 24, 55, 57, 38, 55, 83, 63, 34, 31, 15, 26, 82, 47, 37, 14, 64, 72, 90, 39, 70, 50, 67, 61, 23, 28, 30, 13, 
87, 58, 80, 62, 15, 49, 33, 7, 38, 2, 92, 76, 80, 18, 6, 25, 22, 25, 91, 9, 37, 83, 46, 98, 69, 3, 40, 6, 48, 1, 63, 51, 
32, 19, 77, 74, 22, 75, 41, 19, 27, 82, 60, 6, 1, 55, 5, 71, 18, 84, 47, 16, 1, 8, 41, 6, 17, 100, 62, 36, 45, 32, 4, 33, 
68, 15, 2, 92, 50, 54, 34, 12, 17, 16, 74, 95, 2, 61, 75, 12, 6, 39, 28, 18, 30, 39, 8, 34, 62, 31, 57, 8, 69, 19, 71, 70, 
40, 79, 76, 96, 84, 76, 85, 4, 40, 64, 45, 11, 46, 100, 56, 9, 86, 5, 78, 81, 18, 70, 76, 46, 85, 69, 64, 88, 17, 91, 49, 
93, 18, 29, 38, 42, 77, 63, 46, 32, 83, 88, 48, 68, 89, 80]

for x in range(68):
    print(x)
    if x == 68:
        break
    #print("hey there")
#print("All done and good!")