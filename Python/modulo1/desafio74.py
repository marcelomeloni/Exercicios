
'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

'''
maior = -1
menor = 99999999999
c = 0
import random
numeros = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10) , random.randint(0,10))
for n in numeros:
    if numeros[c] > maior:
        maior = numeros[c]
    elif numeros[c] < menor:
        menor = numeros[c]
    c += 1
print(f'{numeros}\nO maior número da tupla é o {maior} e o menor {menor}')
