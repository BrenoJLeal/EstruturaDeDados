lista_n = [1, 1, 1, 2, 3, 4, 5]
sem_repetidos = []

for elemento in lista_n:
    if elemento not in sem_repetidos:
        sem_repetidos.append(elemento)

print(f'Agora sem números repetidos: {sem_repetidos}')