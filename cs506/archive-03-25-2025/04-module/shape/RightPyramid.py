import Triangle as t
import Square as s

class RightPyramid(t.Triangle, s.Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(base) # this is for square area
    
    def area(self): # surface area
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

rp = RightPyramid(16, 17)
print("total surface area: ", rp.area())
