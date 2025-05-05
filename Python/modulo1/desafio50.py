'''
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''
s = 0
cont = 0

for c in range(1,7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        s += num
        cont += 1
print('A soma dos {} valores é de: {}'.format(cont, s))
