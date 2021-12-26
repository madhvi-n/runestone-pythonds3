def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

def lcm(x, y):
    n = (x*y) // gcd(x, y)
    return n

class Fraction:
    """Class Fraction"""

    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr(self):
        return f"({self.numerator}/{self.denominator})"

    def __add__(self, other_fraction):
        if self.denominator == other_fraction.denominator:
            return Fraction((self.numerator + other_fraction.numerator)/self.denominator)
        new_numerator = (self.numerator * other_fraction.denominator) + (other_fraction.numerator * self.denominator)
        new_denominator = (self.denominator * other_fraction.denominator)
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator/common, new_denominator/common)

    def __sub__(self, other_fraction):
        if self.denominator == other_fraction.denominator:
            return Fraction((self.numerator - other_fraction.numerator)/self.denominator)
        new_numerator = (self.numerator * other_fraction.denominator) - (other_fraction.numerator * self.denominator)
        new_denominator = (self.denominator * other_fraction.denominator)
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator/common, new_denominator/common)

    def __mul__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator/common, new_denominator/common)

    def __truediv__(self, other_fraction):
        if self.denominator == other_fraction.denominator:
            return Fraction(self.numerator, other_fraction.numerator)
        return self.__mul__(Fraction(other_fraction.denominator, other_fraction.numerator))

    def __reduce__(self):
        common = gcd(self.numerator, self.denominator)
        return Fraction(self.numerator/common, self.denominator/common)

    def __eq__(self, other_fraction):
        new_f1 = self.__reduce__()
        new_f2 = other_fraction.__reduce__()
        if new_f1.denominator == new_f2.denominator:
            return new_f1.numerator == new_f2.numerator
        common = gcd(new_f1.denominator, new_f2.denominator)
        return new_f1.numerator * common == new_f2.numerator * common and\
            new_f1.denominator * common == new_f2.denominator * common

    def __ne__(self, other_fraction):
        return not self.__eq__(other_fraction)

    def __gt__(self, other_fraction):
        new_f1 = self.__reduce__()
        new_f2 = other_fraction.__reduce__()
        if new_f1.denominator == new_f2.denominator:
            return new_f1.numerator > new_f2.numerator
        common = gcd(new_f1.denominator, new_f2.denominator)
        return new_f1.numerator * common > new_f2.numerator * common


    def __gte__(self, other_fraction):
        return self.__gt__(other_fraction) or self.__eq__(other_fraction)


    def __lt__(self, other_fraction):
        new_f1 = self.__reduce__()
        new_f2 = other_fraction.__reduce__()
        if new_f1.denominator == new_f2.denominator:
            return new_f1.numerator < new_f2.numerator
        common = gcd(new_f1.denominator, new_f2.denominator)
        return new_f1.numerator * common < new_f2.numerator * common

    def __lte__(self, other_fraction):
        return self.__lt__(other_fraction) or self.__eq__(other_fraction)

    def type(self):
        if not self.denominator == 0:
            if self.numerator == 1:
                return "Unit fraction"
            elif self.numerator < self.denominator:
                return "Proper fraction"
            elif self.numerator > self.denominator:
                return "Improper fraction"
        return "Not defined"


def main():
    f1 = Fraction(4, 5)
    print(f"Fraction f1: {f1}")

    f2 = Fraction(6, 10)
    print(f"Fraction f2: {f2}")

    s = f1.__add__(f2)
    print(f"Sum f1 + f2: {s}")

    sub = f1.__sub__(f2)
    print(f"Subtraction f1 - f2: {sub}")

    m = f1.__mul__(f2)
    print(f"Multiplication f1 * f2: {m}")

    d = f1.__truediv__(f2)
    print(f"Division f1 / f2: {d}")

    e = Fraction(45, 99).__reduce__()
    print(f"{Fraction(45, 99)} when reduced becomes: {e}")

    f = f1.__eq__(f2)
    print(f"Are f1 and f2 equal? {f}")

    f3 = Fraction(4, 3)
    f4 = Fraction(20, 15)

    g = f3.__eq__(f4)
    print(f"f3 equals f4? {g}")

    h = f3.__ne__(f4)
    print(f"f3 not equals f4? {h}")

    i = Fraction(12, 0)
    print(i)
    print(i.type())

if __name__ == '__main__':
    main()
