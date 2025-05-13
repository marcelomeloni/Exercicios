'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada

     
'''

from time import sleep

def contador(inicio, fim, passo):
    print('-' * 30)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')

    if passo == 0:
        passo = 1  # evita passo zero

    if inicio < fim:
        for i in range(inicio, fim + 1, abs(passo)):
            print(i, end=' ', flush=True)
            sleep(0.3)
    else:
        for i in range(inicio, fim - 1, -abs(passo)):
            print(i, end=' ', flush=True)
            sleep(0.3)
    print('\n' + '-' * 30)


# Testes automáticos
contador(1, 10, 1)
contador(10, 0, 2)

# Contagem personalizada
print('Agora é sua vez de personalizar a contagem:')
ini = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(ini, f, p)
