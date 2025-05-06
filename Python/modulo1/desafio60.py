'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. '''
num = int(input('Digite um número para calcular o seu fatorial: '))
fatorial = 1
contador = num

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f'O fatorial de {num} é {fatorial}')

