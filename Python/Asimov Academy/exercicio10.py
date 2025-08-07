'''
Vamos para o último desafio: crie uma função que retorna uma letra do alfabeto, dado o seu índice. 
Por exemplo, o índice 1 deve retornar a letra "A", o índice 2 deve retornar a letra "B" e assim por diante. 
Caso o índice esteja acima ou abaixo dos limites do alfabeto, a função deve retornar um string vazio.
'''

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def retornar_letra(i):
    letra = ""
    indice = 0
    indice = i - 1
    letra = alfabeto[indice]
    return letra

letra_escolhida = int(input("Digite a letra para verificar o indice: "))
if (letra_escolhida > 26):
    print("Digite um valor abaixo de 27.")
elif (letra_escolhida < 1):
    print("Digite um valor acima de 1")
else:
    print(retornar_letra(letra_escolhida))
