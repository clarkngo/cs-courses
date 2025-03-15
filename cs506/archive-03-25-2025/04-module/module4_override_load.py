# 
# -- operator overloading
#

''' Polymorphism: operator overloading by showing +, -, >, <, == on X, Y pair '''
class Point:
    ''' The class that draws a horizontal line  based on number of points'''

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    # Suppose we want the print() function to print the coordinates of the Point object 
    # instead of what we got. We can define a __str__() method in our class that controls 
    # how the object gets printed. Let's look at how we can achieve this:
    # Redefining p1.__str__() --> our point coordinate system
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    # redefining __add__ function to overload an existing operator
    def __add__(self, rhs):
        x = self.x + rhs.x
        y = self.y + rhs.y
        return Point(x, y) # returns a new object
    # redefining __sub__ function to overload an existing operator
    def __sub__(self, rhs):
        x = self.x - rhs.x
        y = self.y - rhs.y
        return Point(x, y) # returns a new object

    # redefining __eq__ function to overload an existing operator
    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y
    # redefining __gt__ function to overload an existing operator
    def __gt__(self, rhs):
        return self.x > rhs.x and self.y > rhs.y
    # redefining __lt__ function to overload an existing operator    
    def __lt__(self, rhs):
        return self.x < rhs.x and self.y < rhs.y

p1 = Point(13, 15)
p2 = Point(-1, 8)

print(p1)
print(p2)
print(p1 + p2) # p1+p2 ==> p1.__add__(p2), p1 <- self, p2 <- rhs
print(p1 - p2)
p3 = p1 - p2
print(p1 > p2)
print(p1 < p2)
print(p1 == p2)


#
# -- method overriding
#
class BaseClass1:
    ''' Class definition of BaseClass2 '''
    def __init__(self):
        # Python caches integers in the range [-5, 256], so it is expected that integers in that range are also identical
        self.x = 0
        self.y = 0

    def add_print_me(self):
        self.x += 100
        self.y += 100        
        print("print x from BaseClass1\n", self.x, self.y, id(self), id(self.x), id(self.y))

    # add 10 to member variables        
    def add10(self):
        self.x += 10        
        self.y += 10                

class BaseClass2:
    ''' Class definition of BaseClass2 '''
    def __init__(self):
        self.x = -10
    
    def add_print_me(self):
        self.x += 1000
        print("print x from BaseClass2\n", self.x, self.y, id(self), id(self.x), id(self.y))

class DerivedClass (BaseClass1, BaseClass2):
    ''' Class definition of DerivedClass '''
    def __init__(self):
        BaseClass1.__init__(self)
        BaseClass2.__init__(self)        
        # super().__init__() #

    def add_print_me(self):
        print("print x from DerivedClass\n", self.x, self.y, id(self), id(self.x), id(self.y))

d1 = DerivedClass()
d1.add_print_me()
d1.add10()
d1.add_print_me()

#   
# -- method overloading
#
class Area:
    def computeArea(self, x = None, y = None):
        area = 0
        # 2 arguments
        if x != None and y != None:
            area = x * y
        # 1 arguments
        elif x != None:
            area = x * x
        return area
            
obj = Area()

print("Area Value:", obj.computeArea())
print("Area Value:", obj.computeArea(4))
print("Area Value:", obj.computeArea(3, 5))

