          #Declare a class
class MyPet():
    # Declare parameters
     name = ''
     age = 1

#Create a object
dog = MyPet()

#Print parameters
print(dog.name)
print(dog.age)

#Change parameters
dog.name = 'Rex'
dog.age = 23

#Print parameters
print(dog.name)
print(dog.age)


# Declare a class
class Person:
    # declare parameters with __init__
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print('Hi my name is', self.name)


p1 = Person('Ion', 16)

print(p1.name)
print(p1.age)
p1.say_hi()

# class Person:
#     # Declare parameters with __init__
#     def __int__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         print('Hi my name is', self.name)
#
#
# p1 = Person()
# p1.say_hi()


