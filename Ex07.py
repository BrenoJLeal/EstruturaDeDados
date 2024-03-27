def n_inteiro(lista):
    segundo = []
    terceiro = []
    menor = lista[0]

    for i in lista:
        if i > menor:
            menor = i
    for i in lista:
        if i != menor:
                segundo.append(i)

    menor2 = segundo[0]
    for i in segundo:
        if i > menor2:
            menor2 = i

    for i in segundo:
        if i != menor and i !=menor2:
            terceiro.append(i)

    menor3 = terceiro[0]
    for i in terceiro:
        if i > menor3:
            menor3 = i
    return menor3
print(n_inteiro([10,3,3,3,4,4,3,4,5,6,4,4,4,4,4,4,3,3,3,3,3]))