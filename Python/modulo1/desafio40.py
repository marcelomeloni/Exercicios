'''

Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2
status = ''
if media < 5:
    status = 'REPROVADO'
elif media <= 6.9:
    status = 'RECUPERAÇÃO'
else:
    status = 'APROVADO'

print('A media do aluno foi {}\nO aluno está em staus de {}'.format(media, status))
