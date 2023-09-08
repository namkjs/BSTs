# Trune.py

import math

def factorial(n):
    """Tính giai thừa của một số nguyên dương n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_prime(number):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Tính diện tích hình chữ nhật."""
        return self.width * self.height

    def perimeter(self):
        """Tính chu vi hình chữ nhật."""
        return 2 * (self.width + self.height)

def greet(name):
    """Chào mừng một người bằng tên."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("This is the advanced_module. Run this module directly to see sample outputs.")
