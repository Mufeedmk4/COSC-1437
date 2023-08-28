# CODE IS CONTINUATION OF CODE FROM CHAPTER 9 RATIONAL ON REVEL 
# AS PER INSTUCTIONS "In addition to the functionality that we implemented in class, your code should conform to the following specifications."
# I HAVE ADDED FUNCTIONALITY 

class Rational:
    def __init__(self, numerator=0, denominator=1):
        divisor = gcd(numerator, denominator)
        if denominator < 0:
            divisor = -divisor
        self.__numerator = numerator // divisor
        self.__denominator = abs(denominator // divisor)

    # Made these methods so we can access the private attirbutes __numerator and __denominator
    def get_numerator(self):
        return self.__numerator
    def get_denominator(self):
        return self.__denominator
    
    # Add a rational number to this rational number
    # Made changes to existing code, by using the previously defined get_ methods
    def __add__(self, secondRational):
        n = self.__numerator * secondRational.get_denominator() + \
            self.__denominator * secondRational.get_numerator()
        d = self.__denominator * secondRational.get_denominator()
        return Rational(n, d)

    # Subtract a rational number from this rational number
        # Made changes to existing code, by using the previously defined get_ methods
    def __sub__(self, secondRational):
        n = self.__numerator * secondRational.get_denominator() - \
            self.__denominator * secondRational.get_numerator()
        d = self.__denominator * secondRational.get_denominator()
        return Rational(n, d)

    # Multiply a rational number to this rational 
        # Made changes to existing code, by using the previously defined get_ methods
    def __mul__(self, secondRational):
        n = self.__numerator * secondRational.get_numerator()
        d = self.__denominator * secondRational.get_denominator()
        return Rational(n, d)

    # Divide a rational number by this rational number
        # Made changes to existing code, by using the previously defined get_ methods
    def __truediv__(self, secondRational):
        n = self.__numerator * secondRational.get_denominator()
        d = self.__denominator * secondRational.get_numerator()
        return Rational(n, d)
    
    # Return a float for the rational number
    def __float__(self):
        return self.__numerator / self.__denominator 

    # Return an integer for the rational number
    def __int__(self):
        return int(self.__float__())

    # Return a string representation  
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
    
    """Fixed cmp with floats as I had used cmp from the textbook chapter 9 under Rational Class Case Study """
    
    def __eq__(self, secondRational):
        return self.__numerator == secondRational.get_numerator() and \
               self.__denominator == secondRational.get_denominator()

    def __ne__(self, secondRational):
        return not self.__eq__(secondRational)
    
    def __pow__(self, power):
        """__pow__ is the dunder method that will take the rational number
        and raise it to the the power 'power' IF its NOT a rational. If it is
        then itll conver it to a float first and then do the power function"""
        
        """ Fixed pow function for proper value"""
        if type(power) == Rational:
            power = float(power)

        numerator = abs(self.__numerator) ** abs(power)
        denominator = self.__denominator ** abs(power)

        if power < 0:
            return Rational(denominator, numerator)
        else:
            return Rational(numerator, denominator)
        
 
    def __abs__(self):
        """__abs__ is the dunder method that will return the abslute value of the rational number"""
        return Rational(abs(self.__numerator), self.__denominator)
   
    # Compare two numbers
    def __cmp__(self, secondRational): 
        temp = self.__sub__(secondRational)
        if temp.get_numerator() > 0:
            return 1
        elif temp.get_denominator() < 0:
            return -1
        else:
            return 0        

def gcd(n, d):
    n1 = abs(n);
    n2 = abs(d)
    gcd = 1
    
    k = 1
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1

    return gcd

if __name__ == "__main__":
    p = Rational(2, 3)
    q = Rational(-5, 7)
    


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