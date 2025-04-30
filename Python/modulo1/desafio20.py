# Sorteando uma ordem na lista

from random import shuffle

a1 = str(input('Primeiro aluno: \n'))
a2 = str(input('Segundo aluno: \n'))
a3 = str(input('Terceiro aluno: \n'))
a4 = str(input('Quarto aluno: \n'))

lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será:\n{}'.format(lista))
