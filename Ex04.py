list_inteiro = list(range(1,10,1))

soma = 0
contador = 0

for numero in list_inteiro:
    soma += numero
    contador +=1

media = soma/ contador

print(f'A media é: {media}')