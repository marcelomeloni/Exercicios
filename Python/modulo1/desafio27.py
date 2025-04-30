# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome: '))
nome = n.split()

print('Primeiro nome: {}'.format(nome[0]))
print("Ultimo nome: {}".format(nome[len(nome)-1]))
