##import math
##
##class ComplexNumber:
##    def __init__(self, real, imaginary):
##        self.real = real
##        self.imaginary = imaginary
##        self.z = complex(self.real, self.imaginary)
##
##    def __eq__(self, other):
##        return complex(self.real, self.imaginary)
##
##    def __add__(self, other):
##        return complex((self.real + other.real),(self.imaginary + other.imaginary))
##
##    def __mul__(self, other):
##        return complex((self.real * other.real - self.imaginary * other.imaginary), (self.imaginary * other.real + self.real * other.imaginary))
##
##    def __sub__(self, other):
##        return complex((self.real - other.real),(self.imaginary - other.imaginary))
##
##    def __truediv__(self, other):        
##        return complex(((self.real * other.real + self.imaginary * other.imaginary)/(other.real**2 + other.imaginary**2)), ((self.imaginary * other.real - self.real * other.imaginary)/(other.real**2 + other.imaginary**2)))
##
##    def __abs__(self):
##        return int(abs(self.z))
##
##    def conjugate(self):
##        return complex(self.real,-self.imaginary)
##
##    def exp(self):
##        return math.e**complex(self.real, self.imaginary)
    
import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return (self.real == other.real) and (self.imaginary == other.imaginary)

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)
        else:
            # other is an int or a float
            return ComplexNumber(other * self.real, other * self.imaginary)

    def __rmul__(self, other):
        return self * other        

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            return (1 / (other.real ** 2 + other.imaginary ** 2)) * (self * other.conjugate())
        else: 
            # other is an int or float
            return ComplexNumber(self.real / other, self.imaginary / other)

    def __abs__(self):
        return math.hypot(self.real, self.imaginary)

    def __repr__(self):
        return f'ComplexNumber({self.real}, {self.imaginary})'

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        return ComplexNumber((math.e ** self.real) * math.cos(self.imaginary), (math.e ** self.real) * math.sin(self.imaginary))
