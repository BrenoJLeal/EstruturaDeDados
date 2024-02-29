class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        aumento = self.salario * (1 + percentual_aumento / 100)
        self.salario = aumento
        return aumento

funcionario = Funcionario('Breno', 5000, 'Desenvolvedor Web')
print(funcionario.aumentar_salario(10))