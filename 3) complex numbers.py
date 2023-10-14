
class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image
    
    def show(self):
        print(self.real, "+", self.image, "i")
    
    def sum(self, other):
        new_real = self.real + other.real
        new_image = self.image + other.image
        
        new_com = Complex(new_real, new_image)
        return new_com

    def sub(self, other):
        new_real = self.real - other.real
        new_image = self.image - other.image
        
        new_com = Complex(new_real, new_image)
        return new_com
    
    def mul(self, other):
        new_real = (self.real * other.real) - (self.image * other.image)
        new_image = (self.image * other.real) + (self.real * other.image)

        new_com = Complex(new_real, new_image)
        return new_com


a = Complex(5, 8)
a.show()

b = Complex(2, 3)
b.show()

c = a.sum(b)
c.show()

d = a.sub(b)
d.show()

e = a.mul(b)
e.show()