def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista if i < pivo]
        iguais = [i for i in lista if i == pivo]
        maiores = [i for i in lista if i > pivo]
        return quicksort(maiores) + iguais + quicksort(menores)

def calcular_mediana(vetor):
    vetor_ordenado = quicksort(vetor)
    meio = len(vetor_ordenado) // 2

    if len(vetor_ordenado) % 2 == 0:
        return (vetor_ordenado[meio - 1] + vetor_ordenado[meio]) / 2.0
    else:
        return vetor_ordenado[meio]


vetor = [7, 8, 9, 5, 1, 2, 2, 3, 4, 5]
mediana = calcular_mediana(vetor)
print("A mediana do vetor é:", mediana)