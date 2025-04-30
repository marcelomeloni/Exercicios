import random
# Recebendo nome dos alunos
a1 = str(input('Digite o nome do primeiro aluno: \n')) 
a2 = str(input('Digite o nome do segundo aluno: \n')) 
a3 = str(input('Digite o nome do terceiro aluno: \n')) 
a4 = str(input('Digite o nome do quarto aluno: \n')) 

lista = [a1, a2, a3, a4]

escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
