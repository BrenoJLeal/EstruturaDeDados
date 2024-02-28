nomes = []
a = []
for nome in range(4):
    nome = str(input('Digite um nome: '))
    nomes.append(nome)

for nome in nomes:
    if nome[0].upper() == 'A':
        a.append(nome)
print(f'Os nomes que começam com A são: {a}')

