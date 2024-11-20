class BaseClass:
    # class definition
    # pass
    def __init__(self):
        self.x = 0
    
    def __private_print(self): # defining a private method
        print("private method from BaseClass")
        print("print x from BaseClass\n", self.x, id(self), id(self.x))

    def print_me(self):
        self.x += 10
        self.__private_print() # defining a private method
    
    x: int

class DerivedClass (BaseClass):
    # DerivedClass definition
    # pass
    def __init__(self):
        BaseClass.__init__(self)
        # super().__init__()
    # def print_me(self):
        # print("print me from DerivedClass\n", self.x, id(self), id(self.x))

class Parent:
    def __privatemethod(self): # calling a private method from a public method
        print("private method from Parent")

    def printmethod(self):
        print("printing from Parent class")
        self.__privatemethod()

    def __init__(self):
        print("INIT: printing from Parent class")

    def get_color(self):
        print(Child.color)
        Child.get_color(self)

    count = 0

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def printmethod(self):
        print("printing from Child class")

    def printmethod_child(self):
        # self.printmethod()
        Parent.privatemethod(self)

    def get_color(self):
        print(self.color)
    def set_color(self, c):
        self.color = c
    def get_count(self):
        print(Parent.count)
    
    color = "red"


P = Parent()
P.printmethod()

C = Child()
C.printmethod_child()

#
# Challenge Question:
#
class myint(int):
    def __init__(self, x):
        self.x = x
    def abs(self):
        ret = -1
        if(self.x < 0):
            ret = self.x * -1
        else:
            ret = self.x
        return ret



# I need to write a class that computes the area
# for different shapes based on the # of sides which would differentiate
# various forms of shapes, circle (1 side), retangle (2 sides), etc.while
# taking the measurements from the user.
#
# My thought process would be, because of the different shapes
# it is difficult to accomplish this with one class, thus inheritance 
# makes sense.
#
# I'll create a generic class called [Shape]
# then I'll add specific attributes its child class e.g. [Rectangle], [Circle]
# So, computing area can be implemented differently 
#
# Here is the steps.
# -- __init__()
# 1. take the # of sides in the constructor __init__()
#    Circle(1), Rectangle(2), Triangle(3) Square(1) etc...
# 2. store the # of sides to one of the member var.
# 3. inside __init__, initialize a list that will hold length information
#
# -- inputSides()
# 4. takes the input from the user and store the lengths into the member list
#    e.g. looping thru float(input('enter a value'))
#
# -- printSides()
# 5. simply print the values as looping thru 
#
# I will then inherit Rectangle from Shape
# 
# -- computeArea()
# 6. this will provide different implementation (polymorphism) via function overriding
#
class Shape:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        for i in range(no_of_sides):
            self.sides.append(0) # initialize

    def inputSides(self):
        for i in range(self.n):
            x = float(input("Enter side "+str(i+1)+" : "))
            self.sides[i] = x

    def printSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])
    sides=[]
   
class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self, 2)

    def computeArea(self):
        x = self.sides[0]
        y = self.sides[1]
        # calculate the perimeter
        area = x * y
        print('The area of the Rectangle is %0.2f' %area)

class Circle(Shape):
    def __init__(self):
        # Shape.__init__(self, 1)
        super().__init__(1)
    
    def computeArea(self):
        r = self.sides
        area = 3.14 * r[0] * r[0]
        print('The area of the Circle is %0.2f' %area)

class Triangle(Shape):
    pass

r = Rectangle()
c = Circle()
c.inputSides()
c.printSides()
c.computeArea()
