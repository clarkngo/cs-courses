import pdb

#
# class a design spec. of what it does.
# 
class Car: # class = blueprint
    ''' a simplest definition of car class '''
    pass

car_john = Car()
car_kate = Car()
car_bob  = Car()

car_john.year = 2004
car_john.color = 'grey'
car_john.model = 'Accord'

car_kate.year = 2015
car_kate.color = 'red'
car_kate.model = 'Edge'

car_bob.year = 2019
car_bob.color = 'silver'
car_bob.model = 'Altima'

print(car_john.year)
print(car_kate.color)
print(car_bob.model)

# 
# -- Let's now add member variables and methods
#
class Car: 
    '''Car class represents a car in year, color, model and speed'''
    num_cars = 0 # class variable that is being shared by all the instances

    def __init__(self, year, color, model, speed): #instance itself
        self.year = year
        self.color = color
        self.model = model
        self.speed = speed
        Car.num_cars += 1 # note that not a self, but class name to access the class var.
 
    def get_year(self):         
        return self.year
    def get_color(self):        
        return self.color
    def get_model(self):        
        return self.model
    def set_speed(self, speed): 
        self.speed = speed
    def is_car_running(self):
        ret = False
        if self.speed > 0:
            ret = True
        return ret
    def printfull(self):            
        return '{} {} {} \tCurrently running at {}'.format(self.year, self.color, self.model, self.speed)
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

    # year: int
    # color: str
    # model: str
    # speed: int

    year  = 2000 # member variable
    color = ''   # member variable
    model = ''   # member variable
    speed = 0    # member variable

car_john = Car(2004, 'grey', 'Accord', 45)
car_kate = Car(2015, 'red', 'Edge', 0)
car_bob  = Car(2019, 'sliver', 'Altima', 65)

print(car_john.year)
print(car_kate.color)
print(car_bob.model)

print(car_john.printfull())
# dir (car_kate) to see all the member var and methods available inside the class.
print(car_kate.is_car_running())
print(car_kate.__dict__) # print member variable in a dict format
print(car_kate.__doc__)  # document string
print(car_kate.__class__)# class name, __name__ in string

#
# -- Let's create a class called Point (2D)
#    I need a class that takes a 2D point, x and y while the object is being created
#    and need 2 methods (1) to modify the existing point with new point (passed in) 
#    and (2) to print the current pair.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def updatePt(self, x, y):
        self.x = x
        self.y = y
    def printPt(self):
        print(f"x = {self.x} y = {self.y}")        

p1 = Point(10, 20)
print(p1.x)

class Point1:
    __x = 0
    __y = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def updatePt(self, x, y):
        self.__x = x
        self.__y = y
    def printPt(self):
        self.__privatePt()

    def __privatePt(self):
        print(f"x = {self.__x} y = {self.__y}")        
        print("privatePt from Point1")

p1 = Point1(10, 20)
print(p1.__x) # cannot directly access the value

#
# -- more data manipulation (sorting via lambda function)
#    on a class member variables
#
class Student:
    ''' this is a student class '''
    def __init__(self, name="", grade="", age=0):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_grade(self):
        return self.grade

    def set_name(self):
        return self.name
    def set_age(self):
        return self.age
    def set_grade(self):
        return self.grade

    def __del__(self):
        class_name = self.__class__.__name__
        # print(class_name, "is out of scope")

    name: str
    age: int

p1 = Student("John", "A", 26)
p2 = Student("Jason", "A", 24)
p3 = Student("Kate", "B", 31)
p4 = Student("Tim", "C", 27)
p5 = Student("Kevin", "B", 33)
p6 = Student("Bob", "B", 29)


print("Student1's name is : ", p1.get_name())
print("Student1's grade is : ", p1.get_grade())
print("Student1's age is : ", p1.get_age())

students = [p1, p2, p3, p4, p5, p6]

# sorted(students, key=lambda student:student.age)
# students.sort(key=lambda student:student.grade)

for s in students:
    print(s.get_name(), s.get_grade())






#
# -- class var to indicate the intial value or
#    default value
class Car:
    model = "no model has been defined" # class var 1 init.
    color = "no color has been defined" # class var 2 init.
    
    def __init__(self, model, color):
        if len(model) > 0:
            self.model = model # updating the instance variable
        if len(color) > 0:
            self.color = color # updating the instnace variable

        print(self.model)
        print(self.color)
        print(model)
        print(color)

# pdb.set_trace()

A = Car(model='Accord', color='')
B = Car(model='', color='White')
C = Car('Cadillac', 'Black')
E = Car('Ferrari', 'Red')
F = Car('Fusion', 'Yellow')
