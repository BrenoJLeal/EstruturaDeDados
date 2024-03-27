def quicksort(lista):
    n = len(lista)
    if n < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista if i < pivo]
        iguais = [i for i in lista if i == pivo]
        maiores = [i for i in lista if i > pivo]
        return quicksort(menores) + iguais + quicksort(maiores)
print(quicksort([9,2,4,5,6,7]))

# def ordenacao(lista):
#     n = len(lista)
#     for i in range(n-1):
#         index=i
#         for j in range(i,n):
#             if lista[j] < lista[index]:
#                 index = j
#         if lista[i] > lista[index]:
#             lista[i], lista[index] = lista[index], lista[i]
# lista = [86,1,24,5,6]
# print(lista)
# ordenacao(lista)
# print(lista)
