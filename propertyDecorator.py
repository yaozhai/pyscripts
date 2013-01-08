from fractions import gcd
from math import atan2, sin, cos

class Rational(object):
    def __init__(self, numer, denom):
        assert denom != 0, 'Denominator can not be 0.'
        g = gcd(numer, denom)
        self.numer = numer // g # '//' result is integer.
        self.denom = denom // g
        
    def __repr__(self):
        return "Rational({0}, {1})".format(self.numer, self.denom)
    
    def __str__(self):
        return "{0}/{1}".format(self.numer, self.denom)
    
    def __add__(self, other):
        return add_rational(self, other)
    
    @property
    def float_value(self):
        return self.numer/self.denom
    
def add_rational(x, y):
    nx, dx = x.numer, x.denom
    ny, dy = y.numer, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    return Rational(x.numer * y.numer, x.denom * y.denom)

class ComplexRI(object):
    def __init__(self, real, image):
        self.real = real
        self.image = image
        
    @property
    def magnitude(self):
        return (self.real ** 2 + self.image ** 2) ** 0.5
    
    @property
    def angle(self):
        return atan2(self.image, self.real)
    
    def __repr__(self):
        return 'ComplexRI({0}, {1})'.format(self.real, 
                                            self.image)
    
class ComplexMA(object):
    def __init__(self, mag, angle):
        self.mag = mag
        self.angle = angle
        
    @property
    def real(self):
        return mag * sin(angle)
    
    @property
    def image(self):
        return mag * cos(angle)
    
    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.mag,
                                            self.angle)

def add_complex(z1, z2):
    return ComplexRI(z1.real + z2.real, 
                     z1.imag + z2.imag)

def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {ComplexRI: 'com',
                 ComplexMA: 'com',
                 Rational:  'rat'}

def add(z1, z2):
    types = (type_tag(z1), type_tag(z2))
    return add.implementations[types](z1, z2)

def add_complex_and_rational(z, r):
    return ComplexRI(z.real + r.float_value, z.image)

def add_rational_and_complex(r, z):
    return add_complex_and_rational(z, r)

add.implementations = {}
add.implementations[('com', 'com')] = add_complex
add.implementations[('rat', 'rat')] = add_rational
add.implementations[('com', 'rat')] = add_complex_and_rational
add.implementations[('rat', 'com')] = add_rational_and_complex