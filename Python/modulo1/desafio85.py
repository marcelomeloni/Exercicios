'''

Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que 
mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.

'''
impares = list()
pares = list()
lista = list()
for i in range(0,7):
    num = int(input('Digite um valor númerico: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
I_qnt = len(impares)
P_qnt = len(pares)
impares.sort()
pares.sort()
for c in range(0,I_qnt):
    lista.append(impares[c])
lista.append('->')
for n in range(0,P_qnt):
    lista.append(pares[n])
print('Pares a esquerda e impares a direita:')
print(lista)
    
    
