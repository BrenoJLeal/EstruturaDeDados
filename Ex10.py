import random
def jogo(escolha):
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    computador = random.choice(opcoes)
    print(f'Você escolheu: {escolha}')
    print(f'O computador escolhe: {computador}')
    if escolha == computador:
        print('Deu empate!')
    elif(
            (escolha == 'Pedra' and computador == 'Tesoura') or
            (escolha == 'Papel' and computador == 'Pedra') or
            (escolha == 'Tesoura'and computador == 'Papel')
    ):
        print('Você ganhou!')
    else:
        print('O computador ganhou!')
escolha = input('Pedra, Papel ou Tesoura ? ').capitalize()

if escolha not in ['Pedra', 'Papel', 'Tesoura']:
    print("Você apenas pode usar Pedra, Papel ou Tesoura ...")
else:
    vencedor = jogo(escolha)
