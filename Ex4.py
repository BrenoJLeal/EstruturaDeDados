class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de {valor} realizado. Novo saldo: {self.saldo}"

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de {valor} realizado. Novo saldo: {self.saldo}"
        else:
            return "Saldo insuficiente."

conta = ContaBancaria(1000, 'Breno Leal')

print(conta.depositar(500))

print(conta.sacar(200))

print(conta.sacar(10000))
