'''

Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.

'''
alunos = dict()

alunos['Nome'] = str(input('Nome: '))
alunos['Media'] = float(input('Media: '))
alunos['Situacao'] = str(input('Situação: '))
print(alunos)
