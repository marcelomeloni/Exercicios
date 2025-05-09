'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

'''

lista = []

for c in range(0,5):
    lista.append(float(input('Digite um valor númerico: ')))
    
lista.sort()
print(f'Lista: {lista} \nMaior valor digitado: {lista[4]}\nMenor valor digitado: {lista[0]}')
