# SCOPE

# Python Scope follows LEGB rules"
# Local, Enlcosing Function Locals, Global, and Built-In

# Local - Names assigned in any way within a function, and not declared global in that function
# EFL (Enclosing Function Locals) - Name in the local scope of any and all enclosing functions from inner to outer
# GLobal - Names assigned at the top-level of a module file, or declared global in a def within the file
# Built-In - Names preassingned in the built-in names module: open, range, SyntaxError, built in methods


#########################################
# In the following example, the first `print(x)` is x printing out the globally known variable because `my_func()` has not yet been declared
# When `my_func()` is called on the following line, and x is now reassigned to 50 within the scope of the function (this is only done within the scope of the function, the global variable if called later will return 25)

# x = 25

# def my_func():
#   x = 50
#   return x

# my_func()
# print(x)


# Local
# lambda x: x**2

# Enclosing function locals
# if we were to comment out the name variable within the greet function, The nested hello function would come then check globally
# name = 'This is a global name!'

# def greet():
#   name = "sammy"

#   def hello():
#     print("hello " + name)
  
#   hello()

# greet()
# print(name)

# MORE LOCAL

# x = 50
# def func(x):
#   print('x is:', x)
#   x = 1000
#   print('local x changed to:', x)

# func(x)
# print(x)

# lets say we wanted to actually change the global value of the code block above
# x = 50
# def func():
#   global x 
#   x = 1000

# print('Before function call, x is:', x)
# func()
# print('After function call, x is:', x)

#############################################################
# OBJECT ORIENTED PROGRAMMING IN PYTHON (OOP)

# mylist is actually an object
mylist = [1, 2, 3]

# append is a built in method of all python objects
mylist.append(4)
print(mylist)

print(type([])) # class list
print(type(())) # class tuple
print(type(20)) # class integer
print(type(20.0)) # class float

# everything in python are objects!!!!
# mylist above is an instance of a list class

# capitalize all of your classes
# class Dog():

#   # CLASS OBJECT ATTRIBUTE
#   species = "mammal"

#   # initialize (constructor), always include self as the first argument
#   def __init__(self, breed, name):
#     self.breed = breed 
#     self.name = name


# my_dog = Dog(breed = "Lab", name = "Sammy") # will throw an error if missing proper arguments for __init__
# # more typically will see it look like the following
# # my _dog = Dog("Lab", "Sammy")
# # other_dog = Dog(breed = "Huskey")

# # print(type(my_dog)) # class __main__.Sample

# print(my_dog.breed)
# print(my_dog.name)
# print(my_dog.species)

class Circle():

  pi = 3.14

  def __init__(self, radius = 1):
      # creates an instance of the .radius attrbiute for circle
      self.radius = radius

  def area(self):
    return self.radius * self.radius * Circle.pi

  def set_radius(self, new_radius):
    self.radius = new_radius

my_c = Circle() # radius defaults to 1
my_c.set_radius(999)
print(my_c.radius)

another_c = Circle(3)
print(another_c.area())

# Inheritance
# Allows for code reuse, inherit things from one class to another
class Animal():

  def __init__(self):
    print("Animal Created")

  def who_am_i(self):
    print("Animal")

  def eat(self):
    print('Eating')

class Dog(Animal):

  def __init__(self):
      # Animal.__init__(self)
      print("Dog Created")
  
  def bark(self):
      print("WOOF!")

  # overides the eat method inherited from the Animal class
  def eat(self):
      print("Dog eating")

my_animal = Animal()

my_animal.who_am_i()
my_animal.eat()

my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()

# SPECIAL METHODS

class Book():

  def __init__(self, title, author, pages):
      self.title = title
      self.author = author
      self.pages = pages

  # we will need to make a string representation to print out the object
  # special methods are denoted with two underscores on either side of the name
  def __str__(self):
      return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

  def __len__(self):
      return self.pages

b = Book("Python", "Jose", 200)
print(b)
print(len(b))
