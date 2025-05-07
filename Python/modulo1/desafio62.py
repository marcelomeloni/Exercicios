'''
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.

'''

# an = a1 + (n-1)r 

n = float(input('Digite a quantidaded e termos da PA:'))
if n == 0:
    print('Programa encerrado')
else:
    a1 = float(input('Digite o primeiro termo da PA: '))
    r = float(input('DIgite a razão da PA: '))
    c = 1
    while c < n+1:
        an = a1 + ((c-1)*r)
        print(an)
        c += 1
