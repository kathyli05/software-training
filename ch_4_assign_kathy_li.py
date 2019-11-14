import math

class Point:
    def __init__ (self, x, y):
        self.x = x 
        self.y = y
    
    def distance(self):
       return math.sqrt(x**2 + y**2)

class Point_3D(Point):
    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def distance(self):
        return math.sqrt(a**2 + b**2 + c**2)

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

    a = input("What is the x-value of your point? \n" )
    if a.isnumeric():
        a = int(a)
    else:
        print("Invalid input.")
        continue

    b = input("what is the y-value of your point? \n")
    if b.isnumeric():
        b = int(b)
    else:
        print("Invalid input.")
        continue

    c = input("What is the z-value of your point? \n")
    if c.isnumeric():
        c = int(c)
    else:
        print("Invalid input.")
        continue
    point_b = Point_3D(a, b, c)
    
    print("The distance from the origin is " + str(point_b.distance()))

    if point_a.distance() > point_b.distance():
        print("The 2D point is further from the origin than the 3D point.")
    elif point_b.distance() > point_a.distance():
        print("The 3D point is further from the origin than the 2D point.")
    elif point_a.distance() == point_b.distance():
        print("The points are the same distance from the origin.")