'''

Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

'''
import random

# Gerar os resultados dos jogadores
jogadores = {
    'Jogador 1': random.randint(1, 6),
    'Jogador 2': random.randint(1, 6),
    'Jogador 3': random.randint(1, 6),
    'Jogador 4': random.randint(1, 6)
}

# Ordenar os jogadores pelo valor do dado em ordem decrescente
placar = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

# Exibir o placar
print("Resultado final:")
for posicao, (jogador, resultado) in enumerate(placar.items(), start=1):
    print(f"{posicao}º lugar: {jogador} com {resultado}")
