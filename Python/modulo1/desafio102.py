'''

Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''
import time

def fatorial(a, show=False):
    f = 1
    for c in range(a, 0, -1):
        if show:
            print(f'{c}', end=' ', flush=True)
            if c > 1:
                print('x', end=' ')
            else:
                print('= ', end='')

            time.sleep(0.5)  # Espera 0.5 segundos antes de continuar
        
        f *= c
    print(f'{f}')

# Exemplo de uso
fatorial(5, show=True)
