positivo = int(input("Digite um número inteiro positivo: "))

if positivo < 0:
    print(f"Digite apenas números positivos!")
else:
    fatorial = 1

    for i in range(1, positivo+1):
        fatorial *= i

    print(f'O fatorial de {positivo} é: {fatorial}')