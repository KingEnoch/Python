'''
This is my 2nd Lab Test for Python!
Date 12-12-2019
Author --> Enoch Oppong
'''
#This import helps me find the square root within the magnitude function
import math

class Vector3D(object):
    """ In the Intializer/Constructor this is where I declare my vector variables"""
    def __init__(self, x, y, z):
        self.x = float(x)#Converting "x" variable into a float
        self.y = float(y)#Converting "y" variable into a float
        self.z = float(z)#Converting "z" variable into a float

    def __str__(self):
        """ This str function will format the output for me. I used the ":f" for formating the float variables x,y,z """
        return "{:f}, {:f}, {:f}".format(self.x, self.y, self.z)

    def __add__(self, other):
        """ This will return a vector that is made by adding two vectors in the format --> (x+a,y+b,z+c) """
        print("Printing Addition")
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """ This will return a vector that is made by subtracting two vectors in the format --> (x-a,y-b,z-c)"""
        print("Printing Subtraction")
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """ This will return a vector that is made by multiply two vectors in the format --> (x*a,y*b,z*c) """
        print("Printing Dot Product")
        print("Printing Integer Multiplication")
        return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __rmul__(self, other):
        """ This is similar to __mul__ but is reversing the effect. It is an int it will multiply in this fashion --> (x*n,y*n,z*n) """
        print("Printing Dot Product")
        print("Printing Integer Multiplication")
        if type(other) == Vector3D:
            return Vector3D(other.x * self.x) + (other.x * self.y) + (other.x * self.z)

    def magnitude(self):
        """ This will return the vector's magnitude in this format --> square root: (x^2+y^2+z^2)"""
        print("Printing In Magnitude!")
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

#This is my printouts
v1 = Vector3D(1,2,3)
v2 = Vector3D(5,5,5)
print("Printing V1")
print("V1 --> ",v1)
print("Printing V2")
print("V2 --> ",v2)
v3 = v1 + v2
print("V1 + V2 --> ",v3)
v4 = v1 - v2
print("v1 - v2 -->",v4)
v5 = v1 * v2
print("V1 * V2 --> ",v5)
v6 = v1 * 2
print("V1 * 2.5 -->",v6)
print("V1 Magnitude is",v1.magnitude())





