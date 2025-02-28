'''import math

class Shape:
    def __init(self,radius,length,breadth):
        self.radius=radius
        self.length=length
        self.breadth=breadth
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(radius):
        return 3.14*(self.radius**2)
    def perimeter(radius):
        return 2*3.14*self.radius
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(length,breadth):
        return self.length*self.breadth
    def perimeter(length,breadth):
        return 2*(self.length+self.breadth)
circle=Circle(2)
circle.area()
circle.perimeter()
rectangle=Rectangle(2,2)
'''

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

shape_type = input("Enter shape (rectangle/circle): ").lower()

if shape_type == "rectangle":
    width = float(input("Enter width : "))
    height = float(input("Enter height : "))
    shape = Rectangle(width, height)
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

elif shape_type == "circle":
    radius = float(input("Enter radius of circle: "))
    shape = Circle(radius)
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

else:
    print("Invalid ")
