import Square as s
class Cube (s.Square):
    def __init__(self, length):
        s.Square.__init__(self, length) # using Square's signature and be able to still find the its parent's class
        #super().__init__(length) # better way to handle (more abstact)
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        face_area = super().area()
        return self.length * face_area

c = Cube (10)
print("Cube Surface Area: ", c.surface_area())
print("Cube Vol.:", c.volume())