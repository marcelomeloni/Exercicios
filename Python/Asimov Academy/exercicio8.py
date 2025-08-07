'''
Você possui uma loja de computadores. No mês passado, suas vendas subiram significativamente. 
Então, você calculou a porcentagem de aumento vendas e anotou o valor como um número (float) em Python:

aumento_vendas = 32.048701

Formate o número em duas casas decimais, exibindo o seguinte texto: "O aumento percentual de vendas foi de 32.05%".
'''

numero = float(input("Digite o número: "))

numero = round(numero, 2)

print(f"O aumento percentual de vendas foi de {numero}%")
