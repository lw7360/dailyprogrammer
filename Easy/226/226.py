# https://www.reddit.com/r/dailyprogrammer/comments/3fmke1/20150803_challenge_226_easy_adding_fractions/

class Fraction():
    def __init__(self, frac_str='0/1'):
        self.frac = tuple([int(i) for i in frac_str.split('/')])

    def __str__(self):
        return str(self.numerator()) + '/' + str(self.denominator())

    def numerator(self):
        return self.frac[0]

    def denominator(self):
        return self.frac[1]

    @staticmethod
    def gcd(a, b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        return Fraction.gcd(b, a%b)

    def __add__(self, other):
        num1 = self.numerator()
        denom1 = self.denominator()
        num2 = other.numerator()
        denom2 = other.denominator()

        num1 *= denom2
        num2 *= denom1
        denom1 *= denom2
        denom2 = denom1

        a = num1 + num2
        b = denom1
        gcf = Fraction.gcd(a,b)
        a /= gcf
        b /= gcf
        return Fraction(str(a) + '/' + str(b))

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

with open('input4.txt') as f:
    x = [Fraction(i.replace('\n','')) for i in f.readlines()[1::]]
    print sum(x)
