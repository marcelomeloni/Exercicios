'''

Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores 
pares sorteados pela função anterior.

'''

numeros = list()
import random
def sorteia(n,m):
    for c in range(0,5):
        numeros.append(random.randint(n,m))
sorteia(1,1000)

def somaPar(numeros):
    soma = 0
    for v in range(0,len(numeros)):
        if numeros[v] % 2 == 0:
            soma += numeros[v]
        
    print(soma)
somaPar(numeros)  
print(numeros)

