'''

Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''

def maior(* num):
    numeros = list()
    for valor in num:
        numeros.append(valor)
    numeros.sort()
    print(f'O maior número é o: {numeros[len(numeros)-1]}')


maior(10,2,3,4)    

maior(32,54,65,76,87,10,2,3,4)    

