'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

import moeda
qnt = int(input('Digite a quantidade de moedas atual: '))
print('''
      LISTA DE OPÇÕES:
      [1]-AUMENTAR
      [2]-DIMINUIR
      [3]-DOBRAR
      [4]-METADE
      ''')
opcao = int(input('DIGITE A OPÇÃO (NUMERO): '))
if opcao == 1:
    print(f'QUANTIDADE DE MOEDAS ATUAL: {moeda.aumentar(qnt)}')
elif opcao == 2:
    print(f'QUANTIDADE DE MOEDAS ATUAL: {moeda.diminuir(qnt)}')
elif opcao == 3:
    print(f'QUANTIDADE DE MOEDAS ATUAL: {moeda.dobrar(qnt)}')
elif opcao == 4:
    print(f'QUANTIDADE DE MOEDAS ATUAL: {moeda.metade(qnt)}')
else:
    print(f'Opção Invalida!')