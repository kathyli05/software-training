import math

class Point:
    def __init__ (self, x, y):
        self.x = x 
        self.y = y
    
    def distance(self):
       return math.sqrt(self.x**2 + self.y**2)

class Point_3D(Point):
    def __init__ (self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

while True:
    x = input("What is the x-value of your point? \n" )

    if x.isnumeric():
        x = int(x)
    else:
        print("Invalid input.")
        continue
        
    y = input("what is the y-value of your point? \n")
    if y.isnumeric():
        y = int(y)
    else:
        print("Invalid input.")
        continue

    point_a = Point(x, y) 
    print("The distance from the origin is " + str(point_a.distance()))

    x = input("What is the x-value of your point? \n" )
    if x.isnumeric():
        x = int(x)
    else:
        print("Invalid input.")
        continue

    y = input("what is the y-value of your point? \n")
    if y.isnumeric():
        y = int(y)
    else:
        print("Invalid input.")
        continue

    z = input("What is the z-value of your point? \n")
    if z.isnumeric():
        z = int(z)
    else:
        print("Invalid input.")
        continue
    point_b = Point_3D(x, y, z)
    
    print("The distance from the origin is " + str(point_b.distance()))

    if point_a.distance() > point_b.distance():
        print("The 2D point is further from the origin than the 3D point.")
    elif point_b.distance() > point_a.distance():
        print("The 3D point is further from the origin than the 2D point.")
    elif point_a.distance() == point_b.distance():
        print("The points are the same distance from the origin.")
    break