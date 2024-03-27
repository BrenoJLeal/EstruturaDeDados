def min_max(lista, key = 'maior'):
    if key == 'maior':
        maior = lista[0]
        for i in lista:
            if i > maior:
                maior = i
        return maior
    elif key == 'menor':
        menor = lista[0]
        for i in lista:
            if i < menor:
                menor = i
        return menor
print(min_max([6,1,3,5,7], 'maior'))
print(min_max([6,1,3,5,7], 'menor'))