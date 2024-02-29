
class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

area = Circulo(5)

print(area.calcular_area())
