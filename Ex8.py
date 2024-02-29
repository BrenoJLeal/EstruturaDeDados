class Aluno:
    def __init__(self, nome, notas=None):
        self.nome = nome
        self.notas = notas if notas is not None else []

    def calcular_media(self):
        if not self.notas:
            n1 = float(input("Digite a primeira nota: "))
            n2 = float(input("Digite a segunda nota: "))
            n3 = float(input("Digite a terceira nota: "))
            self.notas = [n1, n2, n3]

        media = sum(self.notas) / len(self.notas)
        return media


# Example usage:
aluno = Aluno('Breno')
print(aluno.calcular_media())
