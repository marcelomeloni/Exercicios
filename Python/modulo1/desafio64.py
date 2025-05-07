'''
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

'''
n = 0
soma = -999
contador = -1
while n != 999:
    n = int(input('Digite um número inteiro! [999 para parar]'))
    soma += n
    contador += 1
print('Foram digitados {} números até você digitar 999, a soma dentre eles foi: {}'.format(contador, soma))
    
