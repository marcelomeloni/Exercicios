'''
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.

'''
maisPesado = 0
maisLeve = 999

for pessoas in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(pessoas)))
    if peso > maisPesado:
        maisPesado = peso
    if peso < maisLeve:
        maisLeve = peso
print('A pessoa mais leve pesa: {}\nA pessoa mais pesada pesa: {}'.format(maisLeve, maisPesado))
