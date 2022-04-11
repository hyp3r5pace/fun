"""
  3D vector class to store location, direction and color data
"""
import math

class vec3:
    def __init__(self, e1=0, e2=0, e3=0):
        self.append(float(e1))
        self.append(float(e2))
        self.append(float(e3))

    def x(self):
        return self[0]
    def y(self):
        return self[1]
    def z(self):
        return self[2]

    def __neg__(self):
        return vec3(-self[0], -self[1], -self[2])
    
    def __iadd__(self, second):
        self[0] += second[0]
        self[1] += second[1]
        self[2] += second[2]
        return self

    def __imul__(self, scalar):
        self[0] *= scalar
        self[1] *= scalar
        self[2] *= scalar
        return self

    def __idiv_(self, scalar):
        return self *= (1/scalar)

    def length_squared(self):
        return self[0]**2 + self[1]**2 + self[2]**2

    def length(self):
        return math.sqrt(self.length_squared())


    
