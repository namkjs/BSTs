# main.py
from Trune import factorial, is_prime, Rectangle, greet

print(factorial(5))
print(is_prime(17))

rect = Rectangle(4, 6)
print("Rectangle area:", rect.area())
print("Rectangle perimeter:", rect.perimeter())

print(greet("Trunee"))