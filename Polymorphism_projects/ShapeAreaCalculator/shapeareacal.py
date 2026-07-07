class Shape:

    def area(self):
        print("Area is not defined.")


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Circle Area:", area)


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("Rectangle Area:", area)


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        print("Triangle Area:", area)


shapes = [
    Circle(5),
    Rectangle(10, 5),
    Triangle(8, 4)
]

for shape in shapes:
    shape.area()