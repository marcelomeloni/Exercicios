# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input("Qual a velocidade do carro? Em km/h: "))
if velocidade > 80:
    multa = (velocidade - 80)*7 
    print("Você ultrapassou o limite de velocidade, sua multa é de {}R$".format(multa))
else:
    print("Tudo ok! Você está dentro do limite.")
