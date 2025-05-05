'''
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

'''
import random
import time

# definição da lista
jogo = ['PEDRA', 'PAPEL', 'TESOURA']

# cabeçalho
print("JOGO DO JOKENPÔ")
print("-="*20)
print('''
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA''')

# computador escolhe item aleatório da lista
computador = random.choice(jogo)

# jogador escolhe
opcao = int(input('Escolha sua opção: '))

# verificar se opção é válida
if opcao < 1 or opcao > 3:
    print("ESCOLHA UMA OPÇÃO VÁLIDA! (1 a 3)")
else:
    jogador = jogo[opcao - 1]

    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PÔ')

    print("-="*20)
    print(f"Você escolheu {jogador}")
    print(f"O computador escolheu {computador}")
    print("-="*20)

    if jogador == computador:
        print("EMPATE!")
    elif (jogador == 'PEDRA' and computador == 'TESOURA') or \
         (jogador == 'PAPEL' and computador == 'PEDRA') or \
         (jogador == 'TESOURA' and computador == 'PAPEL'):
        print("VOCÊ GANHOU!")
    else:
        print("VOCÊ PERDEU!")
