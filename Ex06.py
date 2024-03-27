def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista if i < pivo]
        iguais = [i for i in lista if i == pivo]
        maiores = [i for i in lista if i > pivo]
        return quicksort(maiores) + iguais + quicksort(menores)
def par_impar(lista):
    par = []
    impar = []
    for i in lista:
        if i%2 == 0:
            par.append(i)
        else:
            impar.append(i)
    return par , impar

lista =[19,23,4,5,6]
lista_ordenada = quicksort(lista)
pares,impares = par_impar(lista_ordenada)
qta_pares = len(pares)
qta_impares = len(impares)
print(lista_ordenada)
print(qta_pares)
print(qta_impares)








