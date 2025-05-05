'''
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

'''
soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0

for i in range(1, 5):
    nome = input(f'Digite o {i}° nome: ')
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = input('Digite o sexo (M para masculino, F para feminino): ').strip().upper()

    soma_idades += idade

    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idades / 4

print(f'\nA média de idade do grupo é {media_idade:.1f} anos.')
print(f'O homem mais velho se chama {nome_homem_mais_velho} e tem {maior_idade_homem} anos.')
print(f'Ao todo, há {mulheres_menos_20} mulher(es) com menos de 20 anos.')
