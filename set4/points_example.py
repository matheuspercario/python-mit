# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 9th, 2021
# ============================================================================
import math


class Point:
    n = 2

    # Methods
    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)  # calcula arctangente

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def add_vectors(self, other):
        new_pt = Point()
        new_pt.x = self.x + other.x
        new_pt.y = self.y + other.y
        return new_pt

    # Magic Methods
    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"


p1 = Point()
p1.x = 3.0
p1.y = 4.0

p2 = Point()
p2.x = 7.0
p2.y = 8.0

print(p1.distance_to_origin())
print(p2.euclidean_distance(p1))
print(p1.manhattan_distance(p2))
print(f"Angle between p2 and p1: {p2.angle_between(p1)}")
print(p1.angle_between(p2))

p3 = p1.add_vectors(p2)
print(f"({p1.x + p2.x}, {p1.x + p1.y})")
print(f"({p3.x}, {p3.y})")
