"""
A class for representing a circle
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def display_circumference(self): #2*3.14*radius
        print(f"Circumference of circle: {2*3.14*self.radius} units.")
    def display_area(self): #3.14*radius*radius
        print(f"Area of circle: {3.14*self.radius**2} square units.")
new_circle = Circle(5)
new_circle.display_circumference()
new_circle.display_area()