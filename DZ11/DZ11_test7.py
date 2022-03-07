class ComplexDigit:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма : {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'Произведение : {self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'


a1 = ComplexDigit(7, 9)
a2 = ComplexDigit(6, 11)
print(a1 + a2)
print(a1 * a2)