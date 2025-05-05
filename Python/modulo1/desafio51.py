'''
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

'''

#An = a1 + (n-1)r 
r = int(input('Digite a razão da PA: '))
a1 = int(input('Digite o primeiro termo da PA: '))
for n in range(1,11):
    print('{}° termo: {}'.format(n, a1+((n-1)*r)))
