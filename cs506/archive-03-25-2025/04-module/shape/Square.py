import Rectangle as r

class Square(r.Rectangle):
    def __init__(self, length):
        r.Rectangle.__init__(self, length, length)
        # super().__init__(length, length)
 

s = Square(10)

print("square area:", s.area())
print("square perimeter:", s.perimeter())