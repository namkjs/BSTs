class Vector:
    """A class for vector"""
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    
a = Vector(2.0,3.0)
print(a)
