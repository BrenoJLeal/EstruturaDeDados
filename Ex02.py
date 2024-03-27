def quick(lista, key = 'Crescente'):
    if len(lista) < 2:
        return lista
    else:
        if key == 'Crescente':
            pivo = lista[0]
            menores = [i for i in lista if i < pivo]
            iguais = [i for i in lista if i == pivo]
            maiores = [i for i in lista if i > pivo]
            return quick(menores) + iguais + quick(maiores)
        elif key == 'Decrescente':
            pivo = lista[0]
            menores = [ i for i in lista if i < pivo]
            iguais = [i for i in lista if i == pivo]
            maiores = [i for i in lista if i > pivo]
            return quick(maiores) + iguais + quick(menores)

print(quick([29,3,5,1], 'Crescente'))
print(quick([29,3,5,1], 'Decrescente'))



# def cresc_decresc(lista, key='crescente'):
#     n = len(lista)
#     for i in range(n-1):
#         index=i
#         for j in range(i,n):
#             if key == 'crescente':
#                 if lista[j] < lista[index]:
#                     index = j
#             elif key == 'decrescente':
#                 if lista[j] > lista[index]:
#                     index = j
#         if key == 'crescente':
#             if lista[i] > lista[index]:
#                 aux = lista[i]
#                 lista[i] = lista[index]
#                 lista[index] = aux
#         elif key == 'decrescente':
#             if lista[i] < lista[index]:
#                 aux = lista[i]
#                 lista[i] = lista[index]
#                 lista[index] = aux
# lista = [9, 4, 1,2 ,4,5]
# print(lista)
# cresc_decresc(lista, 'crescente')
# print(lista)
# cresc_decresc(lista, 'decrescente')
# print(lista)