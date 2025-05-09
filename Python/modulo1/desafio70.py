'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato. 

'''
soma = 0
cont = 0
produto_barato = 999999
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    soma += preco
    if preco < produto_barato:
        produto_barato_nome = nome
        produto_barato = preco
    if preco > 1000:
        cont += 1
    opcao = str(input('Você deseja continuar?: [S/N]')).upper().strip()[0]
    if opcao == 'N':
        print(f'O gasto total nas compras foi: {soma}R$\n{cont} produtos custam mais de 1000R$\nO produto mais barato é {produto_barato_nome}, custando {produto_barato}')
        break
