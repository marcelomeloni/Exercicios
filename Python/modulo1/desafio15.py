# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('Quantos Kms foram percorridos?: '))
day = int(input('Por quantos dias ele foi alugado?: '))

# Calculo da quantidade a pagar

to_pay = (60 * day) + (0.15 * km)

input('O preço a ser pago é de {}R$'.format(to_pay))
