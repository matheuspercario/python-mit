# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 9th, 2021
# ============================================================================

import math


def float_comparison(n1, n2):
    diff = abs(n1 - n2)
    lim = 10 ** (-6)
    if diff > lim:
        return False
    else:
        return True

# Test Function
# print(float_comparison(1.222222454545, 1.222222565656))
# print(float_comparison(1.222222454545, 1.222223545454))


class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Triangle:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def side_lengths(self):
        l1 = self.A.euclidean_distance(self.B)
        l2 = self.A.euclidean_distance(self.C)
        l3 = self.B.euclidean_distance(self.C)
        return l1, l2, l3

    def angles(self):
        a1 = self.A.angle_between(self.C) - self.A.angle_between(self.B)
        a2 = self.B.angle_between(self.A) - self.B.angle_between(self.C)
        a3 = math.radians(180) - (a1 + a2)
        return a1, a2, a3

    def side_classification(self):
        l1, l2, l3 = self.side_lengths()
        if float_comparison(l1, l2) and float_comparison(l1, l3):
            return 'equilateral'
        elif float_comparison(l1, l2) or float_comparison(l1, l3) or float_comparison(l2, l3):
            return 'isosceles'
        else:
            return 'scalene'

    def angle_classification(self):
        a1, a2, a3 = self.angles()
        a1 = math.degrees(a1)
        a2 = math.degrees(a2)
        a3 = math.degrees(a3)
        if float_comparison(a1, a2) and float_comparison(a1, a3):
            return 'equiangular'
        elif 90.0 in (a1, a2, a3):
            return 'right'
        elif a1 < 90 and a2 < 90 and a3 < 90:
            return 'acute'
        elif a1 > 90 or a2 > 90 or a3 > 90:
            return 'obtuse'

    def is_right(self):
        if self.angle_classification() == 'right':
            return True
        else:
            return False

    def perimeter(self):
        return sum(self.side_lengths())

    def area(self):
        p = self.perimeter() / 2
        a, b, c = self.side_lengths()
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    def __str__(self):
        return f"Triangle:\nA -> {self.A}\nB -> {self.B}\nC -> {self.C}"


# Casos de uso
# t = Triangle(Point(15, 0), Point(10, 0), Point(12.5, 4.33))
# t = Triangle(Point(2, 3), Point(5, 6), Point(3, 5))
# t = Triangle(Point(5, 4), Point(5, 1), Point(7, 1))
# print(t)
# print(t.side_lengths())
# print(f"Radianos = \t{t.angles()}")
# a1, a2, a3 = t.angles()
# print(f"Graus = \t\t({math.degrees(a1)}, {math.degrees(a2)}, {math.degrees(a3)})")
# print(t.side_classification())
# print(t.angle_classification())
# print(t.is_right())
# print(t.perimeter())
# print(t.area())
