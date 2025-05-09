
'''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar 
quantas cédulas de cada valor serão entregues. 
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

'''
cinquenta = 0 
vinte = 0 
dez = 0 
um = 0
import math
valor = math.trunc(float(input('Qual valor vai ser sacado?: ')))
while valor - 50 >= 0:
    valor -= 50
    cinquenta += 1
while valor - 20 >= 0:
    valor -= 20
    vinte += 1 
while valor - 10 >= 0:
    valor -= 10 
    dez += 1 
while valor - 1 >= 0:
    valor -= 1 
    um += 1
print(f'{cinquenta} notas de 50R$\n{vinte} notas de 20R$\n{dez} notas de 10R$\n{um} notas de 1R$')
