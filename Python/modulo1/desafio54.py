'''
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''
from datetime import date 

ano_atual = date.today().year

maiores = 0
maisVelho = 9999
maisNovo = 0

for c in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    
    if ano_atual - ano_nascimento >= 18:
        maiores += 1

    # Corrigido: atualiza os valores corretamente
    if ano_nascimento < maisVelho:
        maisVelho = ano_nascimento
    if ano_nascimento > maisNovo:
        maisNovo = ano_nascimento

menores = 7 - maiores

print(f'A quantidade de pessoas maiores na lista é {maiores} e menores é {menores}')
print(f'A pessoa mais velha da lista nasceu em {maisVelho} e a mais nova em {maisNovo}')
