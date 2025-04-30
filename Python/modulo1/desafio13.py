# Novo salario com 15% de desconto

# Definição de variavel e entrada.
salario = float(input('Qual salario do funcionario?: '))
# definindo variavel tipo float caso o salario contenha centavos 

# calculo do aumento
aumento = salario * 0.15


#saida do programa
print('O novo salario para o funcionario é: {}'.format(salario + aumento))
