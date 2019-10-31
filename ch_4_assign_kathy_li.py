import math
class Point:
    def __init__ (self, x, y):
        self.x = x 
        self.y = y
    
    def distance(self):
       return math.sqrt(x**2 + y**2)

class Point_3D(Point):
    def __init__ (self, x, y, z):
        super().__init__(x, y)
        self.z = z 

    def distance(self):
        return math.sqrt(x**2 + y**2 + z**2)

x = int(input("What is the x-value of your point? \n" ))
y = int(input("what is the y-value of your point? \n"))
point = Point(x, y)
print(point.distance())

z = int(input("What is the z-value of your point? \n"))
point = Point_3D(x, y, z)
print(point.distance())

