# day 1
#Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, pi, radius):
        self.pi = pi
        self.radius = radius
         
    def calculate_Area(self):
        return self.pi * self.radius**2
    
    def calculate_parameter(self):
        return 2 * self.pi * self.radius

pi = float(3.14);

radius = float(input("Input the radius of the circle: "));

circle = Circle(pi, radius);

area = circle.calculate_Area();

parameter = circle.calculate_parameter();

print(f"The area of the cirlce is: {area} and the parameter is: {parameter}");





