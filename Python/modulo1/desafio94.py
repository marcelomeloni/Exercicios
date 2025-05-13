'''

Exercício Python 094:
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
'''
dados = dict()
pessoas = list()
soma = 0
mulheres = list()
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [H/M] ')).upper().strip()[0]
    idade = int(input('Idade: '))
    dados = {
        'nome': nome,
        'sexo': sexo,
        'idade': idade
    }
    soma += idade
    if sexo == 'M':
        mulheres.append(dados.copy())
    pessoas.append(dados.copy())
    print('Você deseja continuar?')
    opcao = str(input('Sim/Não: ')).strip().upper()[0]
    if opcao == 'N':
        break 
media = soma/len(pessoas)

print(f'Foram cadastradas {len(pessoas)} pessoas\nA media de idade foi: {media} anos')

print('-='*30)
print('Lista de Mulheres:')
print('-='*30)
for c in range(0,len(mulheres)):
    print(f'Nome: {mulheres[c]["nome"]}')
    print(f'Nome: {mulheres[c]["idade"]}')

for n in range(0,len(pessoas)):
    if pessoas[n]['idade'] > media:
        print(pessoas[n])


