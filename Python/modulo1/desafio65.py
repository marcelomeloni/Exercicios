'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

'''
soma = 0
cont = 0
maiorNumero = 0
menorNumero = 9999999
resposta = 'S'
while resposta == 'S':
    n = int(input('Dígite um número inteiro: '))
    if n < menorNumero:
        menorNumero = n
    elif n > maiorNumero:
        maiorNumero = n
    cont += 1
    soma += n
    resposta = str(input('Você deseja continuar? [S/N]')).upper().strip()[0]
media = soma/cont
if resposta != 'N':
    print('Você deve digitar valores S ou N!')
if resposta == 'N':
    print('A media dos valores lidos foi:{}\nO maior valor lido foi:{}\nO menor valor lido foi:{}'.format(media,maiorNumero,menorNumero))
   
    
