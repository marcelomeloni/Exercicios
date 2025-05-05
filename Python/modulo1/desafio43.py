'''
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida

'''
peso = float(input("Qual seu peso?"))
altura = float(input('Qual a sua altura?'))
imc = peso/(altura*altura)
if imc < 18.5:
    status = "abaixo do peso"
elif imc <= 25:
    status = "peso ideal"
elif imc < 30:
    status = "sobrepeso"
elif imc < 40:
    status = "obesidade"
else:
    status = "obesidade mórbida"
print('Seu IMC é {:.2f} e você está em status de {}'.format(imc, status))
