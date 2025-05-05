'''
Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

'''


import time
for s in range (10, 0, -1):
    print(s)
    time.sleep(1)
print("BOOM! Fogos explodindo!")
