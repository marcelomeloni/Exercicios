'''

Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.

'''
lista = []

for i in range(0,5):
    lista.append(float(input('Digite um valor númerico: ')))
    
lista.sort(reverse=True)

#A) 
print(f'Foram digitados {len(lista)} números!')

#B) 
print(lista)
if lista.count(5) != 0:
    print(f'O valor 5 está na lista! e apareceu {lista.count(5)} vezes')
else:
    print('O valor 5 não esta na lista...')
