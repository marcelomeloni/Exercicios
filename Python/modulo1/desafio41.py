'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''
from datetime import date
ano_atual = date.today().year
ano = int(input('Qual seu ano de nascimento?: '))
idade = ano_atual - ano
if idade <= 9:
    status = 'MIRIM'
elif idade <= 14:
    status = 'INFANTIL'
elif idade <= 19:
    status = 'JÚNIOR'
elif idade <= 25:
    status = 'SÊNIOR'
else:
    status = 'MASTER'
print('Você tem {} anos e se encaixa na categoria {}!'.format(idade,status))
