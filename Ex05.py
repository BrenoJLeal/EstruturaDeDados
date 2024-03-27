def remove_rep(lista):
    sem_repetidos = []

    for i in lista:
        if i not in sem_repetidos:
            sem_repetidos.append(i)
    return sem_repetidos

print(remove_rep([1,1,1,1,2,2,2,23,3,3,3,3]))