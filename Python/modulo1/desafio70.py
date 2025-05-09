'''
xercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato. 

'''
cont = 0
m_mais_20 = 0 
homens = 0 
maiores = 0
while True:
    print('-='*30)
    sexo = str(input('Digite o sexo: [H/M]: ')).upper().strip()[0]
    idade = int(input(f'Digite a idade da {cont+1}° pessoa: '))
    if sexo == 'H':
        homens += 1
    if idade > 18:
        maiores += 1
    if sexo == 'M' and idade < 20:
        m_mais_20 += 1
    print('-='*30)
    print('VOCÊ DESEJA CONTINUAR?')
    opcao = str(input('[SIM/NAO]: ')).upper().strip()[0]
    cont += 1
    if opcao == 'N':
        print(f'Ao todo foram {maiores} pessoas maiores de 18 anos\n{homens} homens\n{m_mais_20} mulheres menores de 20 anos')
        break
    
