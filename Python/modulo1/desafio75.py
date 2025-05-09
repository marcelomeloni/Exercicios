
'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

cont = 0
tupla = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')) )
print(f'O 9 apareceu {tupla.count(9)} vezes, o primeiro valor 3 foi digitado na posição {tupla.index(3)+1}° posição')
for n in tupla:
    if n % 2 == 0:
        cont += 1
print(f'Tiveram {cont} números pares')
