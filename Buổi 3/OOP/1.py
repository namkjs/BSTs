class Shape:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius
    def set_radius(self, radius):
        self.__radius = radius  
    def get_radius(self):
        return self.__radius



circle = Circle("red", 5)
print(circle.get_color())
print(circle.get_radius())
circle.set_color("blue")
circle.set_radius(10)
print(circle.get_color())
print(circle.get_radius())
