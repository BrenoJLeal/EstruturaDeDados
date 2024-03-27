def n_inteiro(lista):
    segundo = []
    menor = lista[0]

    for i in lista:
        if i < menor:
            menor = i
    for i in lista:
        if i != menor:
                segundo.append(i)
    menor2 = segundo[0]
    for i in segundo:
        if i < menor2:
            menor2 = i
    return menor2


print(n_inteiro([10,3,3,3,4,4,3,4,5,6,4,4,4,4,4,4,3,3,3,3,3]))








# def second(lista):
#     menor = min(lista)
#     lista_sem=[]
#
#     for i in lista:
#         if i != menor:
#             lista_sem.append(i)
#     segundo = min(lista_sem)
#     return segundo
# lista = [1,2,3,4,5]
# print(second(lista))

