'''

Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

'''
from datetime import date 
ano = int(input('Em qual ano você nasceu?: '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade == 18:
    print('Você tem {} anos, você está no momento exato para se alistar'.format(idade))
elif idade < 18:
    print('Você tem {} anos, você ainda vai se alistar'.format(idade))
else:
    print('Você tem {} anos, já passou o tempo de você se alistar'.format(idade))
