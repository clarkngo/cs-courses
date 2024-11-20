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
        Shape.__init__(self, 1)
    
    def computeArea(self):
        r = self.sides
        area = 3.14 * r[0] * r[0]
        print('The area of the Circle is %0.2f' %area)

class Triangle(Shape): # class exe.
    def __init__(self):
        Shape.__init__(self, 2)
    
    def computeArea(self):
        b = self.sides[0]
        h = self.sides[1]
        area = b * h * 0.5
        print('The area of the Triable is %0.2f' %area)    


r = Rectangle()
r.inputSides()
r.printSides()
r.computeArea()

c = Circle()
c.inputSides()
c.printSides()
c.computeArea()

t = Triangle()
t.inputSides()
t.printSides()
t.computeArea()
