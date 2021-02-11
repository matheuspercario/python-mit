# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 10th, 2021
# ============================================================================
from math import acos, cos


class Vector:

    # constructor
    def __init__(self, values):
        self.length = len(values)
        self.values = values

    # methods
    def as_list(self):
        return list(self.values)

    def size(self):
        return int(self.length)

    def magnitude(self):
        value = sum([x ** 2 for x in self.as_list()])
        return float(value ** 0.5)

    def euclidean_distance(self, other):
        value = sum(
            [(s - o) ** 2 for s, o in zip(self.as_list(), other.as_list())])
        return float(value ** 0.5)

    def normalized(self):
        m = self.magnitude()
        return Vector([e / m for e in self.as_list()])

    def cosine_similarity(self, other):
        if self.size() == other.size():
            n = self * other
            d = self.magnitude() * other.magnitude()
            return n / d
        else:
            return None

    # Dunder methods
    def __str__(self):
        return str(self.values).replace('[', '<').replace(']', '>')

    def __add__(self, other):
        if isinstance(other, Vector) and self.size() == other.size():
            return Vector([(v_self + v_other) for v_self, v_other in zip(self.as_list(), other.as_list())])
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Vector) and self.size() == other.size():
            return Vector([(v_self - v_other) for v_self, v_other in zip(self.as_list(), other.as_list())])
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Vector) and self.size() == other.size():
            return sum([(v_self * v_other) for v_self, v_other in zip(self.as_list(), other.as_list())])
        elif isinstance(other, (int, float)):
            return Vector([(x * other) for x in self.as_list()])
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector([(x / other) for x in self.as_list()])
        else:
            return None


# Casos de uso --------------------------------------------------
# v = Vector([1, 2, 3, 4, 5, 6, 7])
# v = Vector([3, -5])
# print(v)
# print(v.as_list())
# print(v.size())
# print(v.magnitude())


A = Vector([1, -12, 7.2])
B = Vector([10, -1, 5.32])
C = Vector([10, 24])
D = Vector([1, 7])
E = Vector([1, 7])
# f = 4
# g = 7
# print(A.euclidean_distance(B))
# print(C.normalized())
print(A.cosine_similarity(B))
# print(D + E)
# print(D - E)
# print(D * E)
# print(D * f)
# print(D / f)
