'''

Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.

'''

print('Digite valores para uma matriz 3x3')
m_0 = list()
m_1 = list()
m_2 = list()
variavel = 0
for i in range(0,3):
    num = int(input(f'Digite um valor para a posição [0,{variavel}]'))
    variavel += 1
    m_0.append(num)
variavel = 0
for i in range(0,3):
    num = int(input(f'Digite um valor para a posição [1,{variavel}]'))
    variavel += 1
    m_1.append(num)
variavel = 0  
for i in range(0,3):
    num = int(input(f'Digite um valor para a posição [2,{variavel}]'))
    variavel += 1
    m_2.append(num)
    



print('MATRIZ 3X3')
print('-='*30)
print(m_0)
print(m_1)
print(m_2)
