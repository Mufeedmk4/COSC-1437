class Rational:
    def __init__(self, numerator=0, denominator=1):
        divisor = gcd(numerator, denominator)
        if denominator < 0:
            divisor = -divisor
        self.__numerator = numerator // divisor
        self.__denominator = abs(denominator // divisor)

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def __add__(self, secondRational):
        n = self.__numerator * secondRational.get_denominator() + \
            self.__denominator * secondRational.get_numerator()
        d = self.__denominator * secondRational.get_denominator()
        return Rational(n, d)

    def __sub__(self, secondRational):
        n = self.__numerator * secondRational.get_denominator() - \
            self.__denominator * secondRational.get_numerator()
        d = self.__denominator * secondRational.get_denominator()
        return Rational(n, d)

    def __mul__(self, secondRational):
        n = self.__numerator * secondRational.get_numerator()
        d = self.__denominator * secondRational.get_denominator()
        return Rational(n, d)

    def __truediv__(self, secondRational):
        n = self.__numerator * secondRational.get_denominator()
        d = self.__denominator * secondRational.get_numerator()
        return Rational(n, d)

    def __float__(self):
        return self.__numerator / self.__denominator

    def __int__(self):
        return int(self.__float__())

    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator) + "/" + str(self.__denominator)

    def __lt__(self, secondRational):
        return self.__float__() < float(secondRational)

    def __le__(self, secondRational):
        return self.__float__() <= float(secondRational)

    def __gt__(self, secondRational):
        return self.__float__() > float(secondRational)

    def __ge__(self, secondRational):
        return self.__float__() >= float(secondRational)

    def __eq__(self, secondRational):
        return self.__numerator == secondRational.get_numerator() and \
               self.__denominator == secondRational.get_denominator()

    def __ne__(self, secondRational):
        return not self.__eq__(secondRational)

    def __pow__(self, power):
        if type(power) == Rational:
            power = float(power)

        numerator = abs(self.__numerator) ** abs(power)
        denominator = self.__denominator ** abs(power)

        if power < 0:
            return Rational(denominator, numerator)
        else:
            return Rational(numerator, denominator)

    def __abs__(self):
        return Rational(abs(self.__numerator), self.__denominator)


def gcd(n, d):
    n1 = abs(n)
    n2 = abs(d)
    gcd = 1

    k = 1
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1

    return gcd


if __name__ == "__main__":
    p = Rational(2, -3)
    q = Rational(-2, 3)

    print("p + q =", p + q)
    print("p - q =", p - q)
    print("p * q =", p * q)
    print("p / q =", p / q)
    print("p + 2 =", p + Rational(2))
    print("p + 1.5 =", p + Rational(3, 2))
    print("p * 1.5 =", p * Rational(3, 2))
    print("p / 1.5 =", p / Rational(3, 2))
    print("abs(q) =", abs(q))
    print("p ** 2 =", p ** Rational(2))
    print("q ** -2 =", q ** Rational(-2))

    print("p < q =", p < q)
    print("p <= q =", p <= q)
    print("p == q =", p == q)
    print("p > q =", p > q)
    print("p >= q =", p >= q)
    print("p != q =", p != q)
    print("p > 2 =", p > Rational(2))
    print("p <= p =", p <= p)
    print("p > 0.5 =", p > Rational(1, 2))
