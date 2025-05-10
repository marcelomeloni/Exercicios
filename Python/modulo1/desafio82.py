'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
pares = []
impares = []
for i in range(0,8):
    lista.append(int(input('Digite valores númericos inteiros: ')))
for i in range(0,len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
print(lista)
print(pares)
print(impares)
