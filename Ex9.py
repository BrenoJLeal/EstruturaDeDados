class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
p = Triangulo(4,4,4)
print(p.calcular_perimetro())