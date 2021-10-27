class Square:

    def __init__(self, bok):
        self.bok = bok

class Rectangle:

    def __new__(cls, width:float, height:float):
        if width == height:
            return Square(bok = width)
        return object.__new__(Rectangle)

    def __init__(self,width:float, height:float):
        self.width = width
        self.height = height


r1 = Rectangle(2,7)
r2 = Rectangle(3,3)

print(type(r1))
print(type(r2))