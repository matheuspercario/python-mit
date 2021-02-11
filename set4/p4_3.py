# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 10th, 2021
# ============================================================================

def greatest_common_divisor(a, b):
    """Retorna o maior divisor comum (MDC) entre a e b.

    Args:
        a (int): primeiro valor.
        b (int): segundo valor.

    Returns:
        int: Maior divisor comum (MDC) entre a e b.
    """
    if 0 in (a, b):
        return 1
    if a < b:
        return greatest_common_divisor(a, b - a)
    elif b < a:
        return greatest_common_divisor(a - b, a)
    return a


# print(gdc(18, 12))  # 6
# print(gdc(210, 45))  # 15


class Rational:

    # constructor
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # methods
    def get_numerator(self):
        return int(self.numerator)

    def get_denominator(self):
        return int(self.denominator)

    def to_float(self):
        return float(self.get_numerator() / self.get_denominator())

    def reciprocal(self):
        return Rational(self.get_denominator(), self.get_numerator())

    def reduce(self):
        original = self.get_numerator()
        a = abs(original)
        b = self.get_denominator()
        gdc = greatest_common_divisor(a, b)
        return Rational(original / gdc, b / gdc)

    # Dunder methods
    def __str__(self):
        return f"({self.get_numerator()} / {self.get_denominator()})"

    def __add__(self, other):
        if isinstance(other, (Rational, int)):
            if isinstance(other, int):
                other = Rational(other, 1)

            n = (self.get_numerator() * other.get_denominator()) + \
                (other.get_numerator() * self.get_denominator())
            d = self.get_denominator() * other.get_denominator()
            added = Rational(n, d)
            return added.reduce()

        if isinstance(other, float):
            return float(self.to_float() + other)

    def __sub__(self, other):
        if isinstance(other, (Rational, int)):
            if isinstance(other, int):
                other = Rational(other, 1)

            n = (self.get_numerator() * other.get_denominator()) - \
                (other.get_numerator() * self.get_denominator())
            d = self.get_denominator() * other.get_denominator()
            sub = Rational(n, d)
            return sub.reduce()

        if isinstance(other, float):
            return float(self.to_float() - other)

    def __mul__(self, other):
        if isinstance(other, (Rational, int)):
            if isinstance(other, int):
                other = Rational(other, 1)
            n = self.get_numerator() * other.get_numerator()
            d = self.get_denominator() * other.get_denominator()
            mult = Rational(n, d)
            return mult.reduce()

        if isinstance(other, float):
            return float(self.to_float() * other)

    def __truediv__(self, other):
        if isinstance(other, (Rational, int)):
            if isinstance(other, int):
                other = Rational(other, 1)

            other = other.reciprocal()
            return self * other

        if isinstance(other, float):
            return float(self.to_float() / other)


# Casos de uso -------------------------------------------------------------------
# r = Rational(10, 3)
# r = Rational(15, 30)
# r = Rational(1, 2)
# print(r)
# print(f"{r.get_numerator()} (numerador) \t\t-> {type(r.get_numerator())}")
# print(f"{r.get_denominator()} (denominador) \t-> {type(r.get_denominator())}")
# print(f"{r.to_float()} (to_float) \t\t-> {type(r.to_float())}")
# rec = r.reciprocal()
# print(f"{rec} (inverso) \t-> {type(rec)}")
# reduced = r.reduce()
# print(f"{reduced} (reduced) \t-> {type(reduced)}")
# _r1 = Rational(1, 2)
# _r2 = Rational(1, 3)
# i = 4
# f = 5.0
# print(_r1 + _r2)
# print(_r1 + i)
# print(_r2 + f)
# print(_r1 - _r2)
# print(_r2 - f)
# print(_r1 * _r2)
# print(_r1 * i)
# print(_r1 * f)
# print(_r1 / _r2)
# print(_r1 / i)
# print(_r1 / f)
