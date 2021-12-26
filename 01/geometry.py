"""
Reference: https://realpython.com/python-super/#a-super-deep-dive

"""
from math import sqrt, pi

class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def diagonal(self):
        return sqrt(self.length**2, self.width**2)


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area


class Circle:
    def __init__(self, radius, **kwargs):
        self.radius = radius
        super().__init__(**kwargs)

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius

    def diameter(self):
        return 2 * self.radius


class Sphere(Circle):
    def __init__(self, radius, **kwargs):
        super().__init__(radius=radius, **kwargs)

    def surface_area(self):
        face_area = super().area()
        return face_area * 4

    def volume(self):
        face_area = super().area()
        return (4/3) * self.radius * face_area


def main():
    rect = Rectangle(12, 13)
    print(f"Area of rectangle: {rect.area()}")
    print(f"Perimeter of rectangle: {rect.perimeter()}")

    sqr = Square(12)
    print(f"Area of square: {sqr.area()}")
    print(f"Perimeter of square: {sqr.perimeter()}")

    triangle = Triangle(12, 20)
    print(f"Area of triangle: {triangle.tri_area()}")

    pyramid = RightPyramid(12, 20)
    print(f"Area of pyramid: {pyramid.area()}")
    print(f"Perimeter of pyramid: {pyramid.perimeter()}")

    circle = Circle(10)
    print(f"Diameter of circle: {circle.diameter()}")
    print(f"Area of circle: {circle.area()}")
    print(f"Circumference of circle: {circle.circumference()}")

    sphere = Sphere(8)
    print(f"Diameter of sphere: {sphere.diameter()}")
    print(f"Area of sphere: {sphere.area()}")
    print(f"Volume of sphere: {sphere.volume()}")
    print(f"Surface area of sphere: {sphere.surface_area()}")


if __name__ == '__main__':
    main()


"""
Output:
Area of rectangle: 156
Perimeter of rectangle: 50
Area of square: 144
Perimeter of square: 48
Area of triangle: 120.0
Area of pyramid: 624.0
Perimeter of pyramid: 48
Diameter of circle: 20
Area of circle: 314.1592653589793
Circumference of circle: 62.83185307179586
Diameter of sphere: 16
Area of sphere: 201.06192982974676
Volume of sphere: 2144.660584850632
Surface area of sphere: 804.247719318987
"""
