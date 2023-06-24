# OOPs (Object Oriented Programming)

# Common Words -

# Classes, Objects / Instances / Reference, Methods / Functions

# class Person:
#     # dunder / magic / special methods / contructor
#     def __init__(self):
#         # To initialize instance variables
#         print('Init method is calling.')

# p1 = Person()

# class Person:
#     def __init__(self, first, last):
#         print('Init method is calling.')

#         # instance variables
#         self.first_name = first
#         self.last_name = last

# p1 = Person("Anshul", "Garg")

# print(p1.first_name)
# print(p1.last_name)

class Person:
    def __init__(self, first, last):
        print('Init method is calling.')

        self.first_name = first
        self.last_name = last

    # instance method
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p1 = Person("Anshul", "Garg")
print(p1.full_name())
