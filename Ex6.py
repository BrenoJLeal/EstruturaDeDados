class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def calcular_total(self):
        return self.preco * self.quantidade
produto = Produto('Coca-cola', 8, 5 )
print(produto.calcular_total())