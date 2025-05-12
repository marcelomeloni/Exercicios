'''

Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.

'''
# Inicialização das listas
pessoas = []
maisPesadas = []
maisLeves = []

# Variáveis para armazenar os pesos máximo e mínimo
maiorPeso = menorPeso = 0

while True:
    nome = input("Nome: ").strip()
    peso = float(input("Peso: "))
    
    # Adiciona os dados na lista de pessoas
    pessoas.append([nome, peso])
    
    # Atualiza os valores de maiorPeso e menorPeso
    if maiorPeso == 0 or peso > maiorPeso:
        maiorPeso = peso
    if menorPeso == 0 or peso < menorPeso:
        menorPeso = peso
    
    # Pergunta se deseja continuar
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

# Identifica as pessoas mais pesadas e mais leves
for pessoa in pessoas:
    if pessoa[1] == maiorPeso:
        maisPesadas.append(pessoa[0])
    if pessoa[1] == menorPeso:
        maisLeves.append(pessoa[0])

# Exibe os resultados
print(f"\nForam cadastradas {len(pessoas)} pessoas.")
print(f"As pessoas mais pesadas, com {maiorPeso}Kg, foram: {', '.join(maisPesadas)}")
print(f"As pessoas mais leves, com {menorPeso}Kg, foram: {', '.join(maisLeves)}")
