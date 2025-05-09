'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos. 

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
    
