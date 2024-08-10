# day 1
#Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, pi, radius):
        self.pi = pi
        self.radius = radius
         
    def calculate_Area(self):
        return self.pi * self.radius**2
    
    def calculate_perimeter(self):
        return 2 * self.pi * self.radius

# constant variable that holds the value of pi
pi = float(3.14);

# input section of the value of radius
radius = float(input("Input the radius of the circle: "));

# construction of Object with the provided value of pi and radius
circle = Circle(pi, radius);

# calculation section
# for area using the method calculate_Area() in the object circle
area = circle.calculate_Area();
# for perimeter using the method calculate_Area() in the object circle
perimeter = circle.calculate_perimeter();

print(f"The area of the cirlce is: {area} and the parameter is: {perimeter}");





