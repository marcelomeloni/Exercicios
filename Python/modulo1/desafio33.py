# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Diigite o terceiro valor: '))
if n1 > n2 and n1 > n3:
    maiorvalor = n1
elif n2 > n1 and n2 > n3:
    maiorvalor = n2
else:
    maiorvalor = n3
print('O maior valor entre os três números é: {}'.format(maiorvalor))
