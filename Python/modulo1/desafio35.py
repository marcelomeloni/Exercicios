# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('Verificador de triângulo, digite o tamanho dos segmentos.')
seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))
if seg1 < (seg2 + seg3) and seg2 < (seg1 + seg3) and seg3 < (seg1 + seg2):
    print('O triângulo existe!')
else:
    print('O triângulo não existe!!')
