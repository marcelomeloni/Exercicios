'''

Exercício Python 57: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
import random
tentativas = 1
numero_magico = random.randint(0,10)
numero_usuario = int(input('Tente adivinhar um número de 0 a 10!'))
while numero_magico != numero_usuario:
    if numero_usuario < numero_magico:
        numero_usuario = int(input("Tente novamente! O número é maior!"))
    elif numero_usuario > numero_magico:
        numero_usuario = int(input("Tente novamente! O número é menor!"))
    tentativas += 1
print('Você acertou em {} tentativas! Parabens!'.format(tentativas))
