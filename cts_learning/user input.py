
# age = input('What is your age:? \n')
# print("Your age is " + age + " years old!")


# ########  Made certificate sheet  ##########
pointspossible = 100
studentname = input("Student Name: ")
try:
    score = int(input("Student Score: "))
        ##  score = 0  ## """this is additional syantx we can try and test """
# percent = round(score / pointspossible, 2)   ## """ this is additional syantx we can try and test """
    percent = score / pointspossible
#print("Percentage is {}".format(percent))
    grade = "Error"

# """
# A - 100-90%
# B - 89-80%
# C - 79-70%
# D - 69-60%
# F - 59-0%
# """
#grade = "A"

    if 1 >= percent >= 0.9:
        grade = "A"
    elif 0.9 > percent >= 0.8:
        grade = "B"
    elif 0.9 > percent >= 0.7:
        grade = "C"
    elif 0.9 > percent >= 0.6:
        grade = "D"
    else:
        1 >= percent >= 0.5
    grade = "F"    

###  Print the student name and what grade they got
    print("{} - {}".format(studentname, grade))
except Exception:
    print("Please provide valid number")



######### try and exception case ##############
# try:
#     age = int(input())
#     print("Valid age!")
# except Exception:
#     print("You need to provide a valid number")    