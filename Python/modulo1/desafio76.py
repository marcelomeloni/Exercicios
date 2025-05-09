
'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus 
respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

produtos = ('Pão', 1, 'Melancia', 5, 'Queijo', 30, 'Refrigerante', 10)

print('-=' * 30)
print(f'{"Tabela de Preços":^60}')
print('-=' * 30)

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:.<50} R${preco:>7.2f}')

print('-=' * 30)
