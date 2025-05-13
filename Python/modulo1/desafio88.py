'''

Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa 
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

'''
#Importação do modulo random
import random

#Input
print('-='*30)
jogos = int(input('Quantos jogos vão ser gerados?: '))
print('-='*30)

#Declaração das listas
palpites = list()
jogo = list()


for c in range(0,jogos):
    palpites.clear()
    for d in range(0,6):
        palpite = random.randint(1,60)
        palpites.append(palpite)
    jogo.append(palpites[:])
j = 0   
while j < len(jogo):
    print(f'{j+1}°JOGO: {jogo[j]}')
    j += 1
    
        
