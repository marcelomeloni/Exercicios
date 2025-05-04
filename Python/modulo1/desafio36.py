# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Em quantos anos você deseja pagar?"))
mes = anos*12
prestacao = salario/12
if salario*0.3 < prestacao:
    print('O emprestimo foi NEGADO!!')
else:
    print('O emprestimo foi APROVADO!')
