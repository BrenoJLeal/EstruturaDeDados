n = 3
notas = []
for i in range(n):
    nota = float(input("Digite um valor: "))
    notas.append(nota)

media = sum(notas)/n

print(f"A mádia dos valores é: {media}")