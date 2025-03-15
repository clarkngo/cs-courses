
class Rectangle:
    ''' argument (length and width) '''
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

r = Rectangle(20, 10)

print("rect area:", r.area())
print("rect perimeter:", r.perimeter())