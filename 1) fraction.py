import math

class Fraction:
    def __init__(self, n, d):
        #properties
        self.numerator = n          #numerator: soorate kasr
        self.denominator = d        #denominator: makhraje kasr

    #methods
    def sum(self, fr2):
        num = self.numerator * fr2.denominator + fr2.numerator * self.denominator
        denom = self.denominator * fr2.denominator
        
        x = Fraction(num, denom)
        return x
    
    def sub(self, frac2):
        new_num = self.numerator * frac2.denominator - frac2.numerator * self.denominator
        new_denom = self.denominator * frac2.denominator

        x = Fraction(new_num, new_denom)
        return x

    def mul(self, frac_1):
        result_num = frac_1.numerator * self.numerator
        result_denom = frac_1.denominator * self.denominator

        x = Fraction (result_num, result_denom)
        return x
    
    def div(self, fr2):
        num = self.numerator * fr2.denominator
        denom = self.denominator * fr2.numerator

        x = Fraction(num, denom)
        return x

    def fraction_to_decimal(self):
        decimal = self.numerator / self.denominator

        return decimal
    
    def simplified(self):
        g = math.gcd(self.numerator, self.denominator)      #greatest common divisor of numerator & denominator
        sim_numerator = self.numerator / g
        sim_denominator = self.denominator / g

        x = Fraction(sim_numerator, sim_denominator)
        return x

    def show(self):
        print (self.numerator,"/", self.denominator)

a = Fraction (2, 3)
a.show()
b = Fraction (7, 1)
b.show()
c = Fraction (756, 336)


w = a.sum(b)
w.show()

z = b.mul(a)
z.show()

y = a.sub(b)
y.show()

v = a.div(b)
v.show()

d = a.fraction_to_decimal()
print (d)


s = c.simplified()
s.show()