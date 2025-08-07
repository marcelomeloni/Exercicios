'''
Nesta atividade, você possui uma lista de números qualquer. Por exemplo:

numeros = [32, 10, 58, 30, 55, 12, 28, 51]

Seu objetivo é encontrar o segundo maior valor da lista (supondo que ela possua pelo menos dois elementos).
'''

numeros = [32, 10, 58, 30, 55, 12, 28, 51]

numeros = sorted(numeros)
numeros = numeros[::-1]
print(f'O segundo maior número é: {numeros[1]}')
