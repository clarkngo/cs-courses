class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.height * self.base * 0.5


t = Triangle(5, 10)
print("Triangle area: ", t.area())

    