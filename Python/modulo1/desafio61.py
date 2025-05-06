
''' Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while. '''

# an = a1 + (n-1)r 

a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('DIgite a razão da PA: '))
c = 1
while c < 11:
    an = a1 + ((c-1)*r)
    print(an)
    c += 1
