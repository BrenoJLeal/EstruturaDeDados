lista1 = [1,2,3,4,9]
lista2 = [1,9,5]
listaC = []

for n in lista1:
    if n in lista2:
        listaC.append(n)
print(listaC)
