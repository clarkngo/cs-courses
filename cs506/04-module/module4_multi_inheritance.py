#
# -- multiple inheritance using super()
#
class BaseClass1:
    ''' Class definition of BaseClass2 '''
    def __init__(self):
        # Python caches integers in the range [-5, 256], so it is expected that integers in that range are also identical
        self.x = 0
        self.y = 0
        print("1")

    # adding 100 before printing
    def print_me(self):
        print("print from BaseClass1\n", self.x, self.y)#, id(self), id(self.x), id(self.y))

    # add 10 to member variables        
    def add10(self):
        self.x += 10        
        self.y += 10                

class BaseClass2:
    ''' Class definition of BaseClass2 '''
    def __init__(self):
        self.x = -10
        print("2")
    def print_me(self):
        print("print from BaseClass2\n", self.x)#, id(self), id(self.x), id(self.y))

    def sub1000(self):
        self.x -= 1000

class DerivedClass(BaseClass1, BaseClass2):#, BaseClass1):
    ''' Class definition of DerivedClass '''
    def __init__(self):
        # BaseClass2.__init__(self)        
        # BaseClass1.__init__(self)
        super().__init__() #
        super(BaseClass1, self).__init__()
        super().sub1000()

    def print_me(self):
        print("print from DerivedClass\n", self.x, self.y)#, id(self), id(self.x), id(self.y))

d1 = DerivedClass()
d1.print_me()
d1.add10()
d1.sub1000()
d1.print_me()
