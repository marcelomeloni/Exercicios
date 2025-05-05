'''
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 

'''

frase = str(input('Digite uma frase: ')).strip().upper()

lista = frase.split()

junto = ''.join(lista)

invertido = junto[::-1]

if junto == invertido:
    print("Essa frase é um palíndromo!!")
else:
    print("Essa frase não é um palíndromo!!")

