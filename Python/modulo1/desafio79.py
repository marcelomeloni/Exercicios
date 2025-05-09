'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

lista = []
c = -1
while True:
    n = float(input('Digite um valor númerico: '))
    if n in lista:
        print('O número está na lista!')
    else:
        lista.append(n)
    print(lista)
    opcao = str(input('Você deseja continuar? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
lista.sort()
print(f'A lista fornecida em ordem crescente:')
for c in range(0,len(lista)):
    print(lista[c])
    
