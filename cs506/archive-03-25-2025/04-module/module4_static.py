# Defining static variable and method is a common programming concept and 
# is widely used in C++, Java, Php and many other programming languages for 
# creating class variables and methods that belong to the class and are shared 
# by all the objects of the class.

# In Python, there is no special keyword for creating static variables and 
# methods. Python follows a different but simple approach for defining 
# static variables and methods which we will learn in this tutorial.

# Class or Static Variables in Python
# Class or Static variables are the variables that belong to the class and 
# not to objects. Class or Static variables are shared amongst objects of 
# the class. All variables which are assigned a value in the class declaration 
# are class variables. And variables which are assigned values inside 
# class methods are instance variables.

# This example shows a scenario where there are different shape objects 
# each belonging to the same category which is Geometrical but are of different 
# types, so each object of the class have the same category which we have made 
# the class variable and the type variable is different for all the objects 
# hence it is an instance variable.

# The use case: Static variable and methods are used when we want to define some behaviour or property 
# specific to the class and which is something common for all the class objects.
class Shape:
    # class or static variable 
    cat = 'Geometrical' # defined outside of method -> class var.
    def __init__(self, type):
    # instance variable
        self.type = type # defined inside a method -> object var.

    # method to show data
    def print_shape(self):
        # accessing class variable
        print('Shape is of category: ', Shape.cat)
        # accessing instance variable
        print('And shape is: ', self.type)
    
    # a class method to create an object
    # similarity with static method/class method: bound to a class itself (cls) not its object
    @classmethod
    def createShape(cls, type):
        return cls(type)
        

tr = Shape('Triangle')
sq = Shape('Square')
rec = Shape('Circle')
py = Shape.createShape('Pyramid')

tr.print_shape()
sq.print_shape()
rec.print_shape()
py.print_shape()

# Just like static variables, static methods are the methods which are bound to the class 
# rather than an object of the class and hence are called using the class name 
# and not the objects of the class.
# As static methods are bound to the class hence they cannot change the state of an object.
# To call a static method we don't need any class object, it can be directly called using the class name.
# In python there are two ways of defining a static method:
# Using the staticmethod()
# Using the @staticmethod
# The difference with static method/class method: static doesn't know about the class/just deals with the parameter
# Note that for a static method we don't provide the argument self 
# because static methods don't operate on objects.
class Vehicle:
    seats = "the number of seating "
    @staticmethod
    def seat_info(msg):
        if int(msg) > 0:
            print(Vehicle.seats + "[" + msg + "] seats")

Vehicle.seat_info("0")

class Truck:
    def info(self):
        print("Truck has ", end="")
        Vehicle.seat_info("2")
t = Truck()
t.info()        

class Bus:
    def info(self):
        print("Bus has ", end="")
        Vehicle.seat_info("20")
b = Bus()
b.info()        

class Sedan:
    def info(self):
        print("Sedan has ", end="")
        Vehicle.seat_info("4")
s = Sedan()
s.info()        
