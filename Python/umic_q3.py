import math
class Complex(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def display(self):
        if self.y>0:
            return "%s + %si" %(self.x, self.y)
        else:
            return "%s %si" %(self.x, self.y)
    def add(self,other):
        return Complex(self.x + other.x , self.y+ other.y )
    def subtract(self,other):
        return Complex(self.x - other.x , self.y- other.y )
    def modulus(self):
        return math.sqrt((self.x)**2 + (self.y)**2)
    def multiplication(self,other):
        return Complex(self.x * other.x , self.y * other.y )
    def conjugate(self):
        return Complex(self.x , (self.y)*(-1) )
    def inverse(self):
        return Complex(self.x/Complex.modulus(self) , (self.y)*(-1)/Complex.modulus(self) )
    
    