lista_valores = list(range(10, 60, 10))

print(f'Esses são os valores: {lista_valores}')

maior_valor = lista_valores[0]

for valor in lista_valores:
    if valor > maior_valor:
        maior_valor = valor

print(f'O maior valor é: {maior_valor}')