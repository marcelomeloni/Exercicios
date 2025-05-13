'''

Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
ano_atual = date.today().year
salario = 0
nome = str(input('Digite seu nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
ct = int(input('Ano de contratação: [Se não for contratado digite 0]'))
if ct != 0:
    salario = float(input('Salario: '))
idade = ano_atual - ano_nascimento

trabalhador = {
    'nome': nome,
    'idade': idade,
    'ano_contratacao': ct,
    'salario': salario
}

print(trabalhador)
