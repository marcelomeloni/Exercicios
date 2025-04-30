# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome: ')).strip().lower()
print('Seu nome tem silva? {}'.format(nome.find('silva') != -1))
