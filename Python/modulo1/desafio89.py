'''

Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

'''

alunos = []

while True:
    nome = str(input('Digite o nome do aluno: ')).strip().upper()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media])
    opcao = str(input('Você deseja continuar? [S/N]: ')).strip().upper()
    if opcao == 'N':
        break

# Exibição das médias
print("\nBoletim:")
for aluno in alunos:
    print(f'{aluno[0]}: Média = {aluno[3]:.1f}')

# Consulta de notas
while True:
    nome_consultar = str(input('\nDigite o primeiro nome do aluno para consultar as notas ou "FIM" para encerrar: ')).strip().upper()
    if nome_consultar == 'FIM':
        break
    encontrado = False
    for aluno in alunos:
        if aluno[0].split()[0] == nome_consultar:
            print(f'Notas de {aluno[0]}: {aluno[1]} e {aluno[2]}')
            encontrado = True
            break
    if not encontrado:
        print('Aluno não encontrado.')

