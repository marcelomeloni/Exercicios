'''
Crie um script capaz de detectar palíndromos. 
Um palíndromo é uma palavra que permanece a mesma se for lida de trás para frente, como “arara” ou “radar”.
'''

palavra = input(str("Digite uma palavra: "))

palavra_invertida =  palavra[::-1]

if palavra_invertida == palavra:
    print(f"A palavra {palavra} é um palíndromo")
else:
    print(f"A palavra {palavra} não é um palíndromo.")
