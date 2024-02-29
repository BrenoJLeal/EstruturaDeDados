class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura

calc = Retangulo(5,5)
print(calc.calcular_area())