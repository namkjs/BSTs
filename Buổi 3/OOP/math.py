class Vector:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __repr__(self):
        return f'({self.x}, {self.y})'
    def __add__(self, v):
        x = self.x + v.x
        y = self.y + v.y
        return Vector(x, y)
    def __sub__(self, v):
        x = self.x - v.x
        y = self.y - v.y
        return Vector(x, y)
    def __mul__(self, n):
        x = self.x * n
        y = self.y * n
        return Vector(x, y)
    def __neg__(self):
        return Vector(self.x * -1, self.y * -1)
    
a = Vector(2,1)
b = Vector(3,1)
print(a + b)