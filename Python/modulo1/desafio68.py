'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele 
conquistou no final do jogo. 

'''


import random

escolhas = ['IMPAR', 'PAR']

num = ''
while True:
    computador_num = random.randint(0,10)
    print('-='*30)
    print('Par ou Impar')
    print('-='*30)
    print('Você quer ser IMPAR ou PAR?')
    opcao = str(input('[I/P]?: ')).upper().strip()[0]
    jogador = int(input('Digite seu número: '))
    soma = jogador + computador_num
    if soma % 2 == 0:
        num = 'P'
    else:
        num = 'I'
    if opcao == num:
        print('Você ganhou! Parabéns.')
    else:
        print(f'Você perdeu! :(\nO computador escolheu {computador_num}')
        break
    soma = 0
    
    
