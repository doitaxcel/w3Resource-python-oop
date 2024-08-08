# day 2 - modified
# Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. Implement subclasses 
# for different shapes like circle, triangle, and square.

class Shape():
    def calculateArea():
        pass
    def calculatePerimeter():
        pass
    
class Circle(Shape):
    def __init__(self, pi, radius) -> None:
        self.pi = pi
        self.radius = radius
    
    def calculateArea(self):
        return self.pi * self.radius**2
    
    def calculatePerimeter(self):
        return 2 * self.pi * self.radius
        
class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side
    
    def calculateArea(self):
        return self.side**2
    
    def calculatePerimeter(self):
        return 4*self.side
        
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3) -> None:
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculateArea(self):
        return  1.5 * self.base * self.height
    
    def calculatePerimeter(self):
        return self.side1 + self.side2 + self.side3
        
    
pi = 3.14

while(True):
    try:
        print("What shape do you want to get the area and Perimeter?")
        print("   1. Circle    2. Square    3.Triangle   ")
        chooseShape = int(input("Select: "))
        
        if chooseShape == 1:
            radius = float(input("Input the radius of the circle: "))
            
            circle = Circle(pi, radius)
            Area = circle.calculateArea()
            Perimeter = circle.calculatePerimeter()
            
            print(f"Area: {Area}")
            print(f"Perimeter: {Perimeter}")
            break
        elif chooseShape == 2:
            side = float(input("Input the length of side of the square: "))
            
            square = Square(side)
            Area = square.calculateArea()
            Perimeter = square.calculatePerimeter()
            
            print(f"Area: {Area}")
            print(f"Perimeter: {Perimeter}")
            break
        elif chooseShape == 3:
            base = float(input("Base of the Triangle: "))
            height = float(input("Height of the Triangle: "))
            
            print("Sides input is by clockwise rotate (left to right)")
            side1 = float(input("Side 1:"))
            side2 = float(input("Side 2:"))
            side3 = float(input("Side 3:"))
            
            triangle = Triangle(base, height, side1, side2, side3)
            Area = triangle.calculateArea()
            Perimeter = triangle.calculatePerimeter()
            
            print(f"Area: {Area}")
            print(f"Perimeter: {Perimeter}")
            break
        else:
            print("\n---------Invalid input, choices are from 1 - 3 only---------\n")
            print("                 *** TRY AGAIN ***")

    except ValueError as e:
        #print(f"Invalid input, '{chooseShape}' is not a number")
        #print(f"Invalid input: {e}")
        print("\n---------Input is not a Number---------")
        print("          *** TRY AGAIN ***\n")
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("  *** TRY AGAIN ***\n")