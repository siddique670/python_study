## classes and variables

# class Dog:
#     "hello"
# dog1 = Dog()
# dog1.hellojohn = "Fido"
# dog2 = Dog()
# dog2.name = "Sean"
# dog3 = Dog()

# print(dog1.hellojohn)
# print(dog2.name)


# class Dog:
#     doginfo = "Dogs are animals wit 4 legs and a tail"
# # dog1 = Dog()
# # dog1.hellojohn = "Fido"
# # dog2 = Dog()
# # dog2.name = "Sean"
# # dog3 = Dog()

# # print(dog1.doginfo)
# # print(dog2.doginfo)
# #Dog.doginfo = "Hello"
# print(Dog.doginfo)


## Question :- Create a class named Car and give it a class property named definition. Set it equal to Something with 4 wheels and an engine

# class Car:
#     definition = "Something with 4 wheels and an engine"
# print(Car.definition)


     ###############        init metthod      ##################

# class Dog:

#     def __init__(self):
#             print("hi there")      
# dog1 = Dog()

# class Dog:

#     def __init__(self, name, age, furcolor):    
#         self.name = name
#         self.age = age
#         self.furcolor = furcolor
# dog1 = Dog("Abrar", 29, "Brown")
# print(dog1.age, dog1.name, dog1.furcolor)
# # print(dog1.name)
# # print(dog1.furcolor)
#============================================================================================
## Question:- Add an init function to the Car class that takes the parameters year, make and model. Make all of these instance variables.

## Soulution 

# class Car:
#     def __init__(self, year, make, model):
#         self.year = year
#         self.make = make
#         self.model = model
#     def age(self):
#         return 2016 - self.year
#     print(2016)
# car1 = Car(2022, "BMW", "SU")
# print(car1.year, car1.make, car1.model)


# class Dog:
#     def __init__(self, year, make, model):
#         self.year = year
#         self.make = make
#         self.model = model
#     # def barkhello():
#     #     print("Hello World")   
#     def bargoodbye(self):
#         print("car is " + "(2016 - year)")
# dog1 = Dog(2022, "BMW", "SU")
# print(dog1.year, dog1.make, dog1.model)
# dog1.bargoodbye()
# #Dog.barkhello()
#===========================================================
# class Car:
#     def __init__(self, year, make, model):
#         self.year = year
#         self.make = make
#         self.model = model    
#     def bargoodbye(self):
#         print("car is " + "(2016 - year)")
# car1 = Car(2016, "BMW", "SU")
# print(car1.year, car1.make, car1.model)
# car1.bargoodbye()

############        Inheritance       ##############

# class Dog:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
# class Bulldog(Dog):
#     def growl(self):
#         print("Abrar")
# dog1 = Bulldog("Mike", 22, "White")
# print(dog1.name, dog1.age, dog1.color)
# dog1.growl()
# Question :- Create a class called Mustang, that inherits from Car and has an init function that only asks for year, and sets 
# make = "Ford" and model = "Mustang"
# class Car:
#     def __init__(self,year, make, model):
#         self.year = year
#         self.make = make
#         self.model = model
#     def age():
#         return 2016 

# class Mustang(Car):
#     def age(self):
#         print("2016")
# car1 = Mustang(2016, "Ford", "Mustang")
# print(car1.year, car1.make, car1.model)
# car1.age()

# class Car:
#     def __init__(self,year, make, model):
#         self.year = year
#         self.make = make
#         self.model = model
    
#     def age(self):
#         return 2016 - self.year
# class Mustang(Car):
#      def __init__(self,year, make, model):
#         Car.__init__(self,year, make, model)
#         self.year=year
        
# car1 = Mustang(2016, "Ford", "Mustang")
# print(car1.year)

# class Mustang(Car):

#     wheels = 4

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

# mustang = Car(2016, 'Ford', 'Mustang')
# print(mustang.wheels)
# # 4
# print(Car.wheels)
# 4

## Correct Code:= 
class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
       
    
    def age(self):
        return 2016 - self.year
    
class Mustang(Car):
    def __init__(self,year, make = "Ford", model = "Mustang"):
        Car.__init__(self,year, make, model)
        self.year=year
car1 = Mustang(2016, "Ford", "Mustang")
print(car1.year, car1.make, car1.model)
