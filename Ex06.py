lista_strings = ['Tijolo', 'Programação', 'Kamikaze', 'Estrutura', 'Dados']

maior = ''

for string in lista_strings:
    if len(string) > len(maior):
        maior = string

print(f'A maior string é: {maior}')