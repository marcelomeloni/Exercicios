'''
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros

'''
preco = float(input('Digite o preço do produto: '))

print(''' *** METODO DE PAGAMENTO ***
1 – à vista dinheiro/cheque: 10% de desconto

2 – à vista no cartão: 5% de desconto

3 – em até 2x no cartão: preço formal 

4 – 3x ou mais no cartão: 20% de juros''')

opcao = int(input("Qual sua opção?: "))
valido = 1
if opcao == 1:
    preco = preco*0.9
elif opcao == 2:
    preco = preco*0.95
elif opcao == 3:
    print("O preço a ser pago vai ser duas parcelas de {:.2f}R$".format(preco/2))
    valido = -1
elif opcao == 4:
    preco == preco*1.20
else:
    print('Opção invalida! Tente novamente')
    valido = -1
if valido != -1:
    print('O preço total a ser pago escolhendo a opção {} vai ser {}R$'.format(opcao,preco))
