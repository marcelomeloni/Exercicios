# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

import math

num = int(input('Digite um número: '))
print('O dobro de {} é {}\nO triplo de {} é {}\nA raiz quadrada de {} é {:.3f}'.format(num,num*2, num, num*3, num, math.sqrt(num)))
