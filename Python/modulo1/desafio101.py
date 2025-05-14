'''

Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições
'''
def voto(ano):
    if 2025 - ano < 16:
        return "negado"
    elif 2025 - ano > 18:
        return "obrigatorio"
    else:
        return "opcional"
ano = int(input('Digite seu ano de nascimento: '))
print(f'Sua situação de voto é: {voto(ano)}')
