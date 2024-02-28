lista = []
numeros_pares = []
for n in range(4):
    numeros = int(input("Digite um valor: "))
    lista.append(numeros)

for numero in lista:
    if numero % 2 == 0:
        numeros_pares.append(numero)

if numeros_pares:
    media = sum(numeros_pares) / len(numeros_pares)
    print(f'O resultado da média entre os números pares: {numeros_pares} é {media}')
else:
    print(f'Você não digitou nenhum número par')
