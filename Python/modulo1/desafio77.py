
'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

tupla = ('Pimba', 'Zureta', 'Douro', 'Bancada', 'Rota')

for palavra in tupla:
    print(f'\nNa palavra "{palavra.upper()}" temos as vogais:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
