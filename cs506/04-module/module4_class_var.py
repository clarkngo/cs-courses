import pdb

class Car:
    model = "no model has been defined"
    color = "no color has been defined"
    
    def __init__(self, model, color):
        if len(model) > 0:
            self.model = model
        if len(color) > 0:
            self.color = color

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

