'''
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se 
encontram no intervalo de 1 até 500.
'''
s = 0
cont = 0
for num in range(1,501, 2):
 if num % 3 == 0:
     s += num
     cont +=1
print('A soma dos {} valores é: {}'.format(cont,s))
