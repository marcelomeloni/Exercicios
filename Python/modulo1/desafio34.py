# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.
salario = int(input('Digite o salario do funcionário: '))
if salario > 1250:
    aumento = salario*0.1
else:
    aumento = salario*0.15
print('O aumento do salario é de {}'.format(aumento))
