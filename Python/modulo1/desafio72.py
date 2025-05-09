
'''
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.

'''
while True:
    numero = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

    num = int(input('Digite um número de 0 a 10: '))

    if num > 0 and num < 10:
        print(numero[num].upper())
        break
    else:
        print('Digite um número de 0 a 10!!!')
