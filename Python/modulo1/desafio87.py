'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.

'''
print('Digite valores para uma matriz 3x3')
m_0 = list()
m_1 = list()
m_2 = list()
maior_valor = -9999
variavel = 0
soma = 0
soma_3 = 0
for i in range(0,3):
    num = int(input(f'Digite um valor para a posição [0,{variavel}]'))
    variavel += 1
    m_0.append(num)
    if num % 2 == 0:
        soma += num
    if len(m_0) == 3:
        soma_3 += num
variavel = 0
for i in range(0,3):
    num = int(input(f'Digite um valor para a posição [1,{variavel}]'))
    variavel += 1
    m_1.append(num)
    if num % 2 == 0:
        soma += num
    if len(m_1) == 3:
        soma_3 += num
    if num > maior_valor:
        maior_valor = num
variavel = 0  
for i in range(0,3):
    num = int(input(f'Digite um valor para a posição [2,{variavel}]'))
    variavel += 1
    m_2.append(num)
    if num % 2 == 0:
        soma += num
    if len(m_2) == 3:
        soma_3 += num
    
    



print('MATRIZ 3X3')
print('-='*30)
print(m_0)
print(m_1)
print(m_2)
print('Soma de todos os números pares: {}'.format(soma))
print(f'Soma dos valores da 3° coluna: {soma_3}')
print(f'Maior valor da 2 linha: {maior_valor}')
