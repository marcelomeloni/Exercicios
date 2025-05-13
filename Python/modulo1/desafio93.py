'''

Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

nome = str(input('Nome do jogador: '))
partidas = int(input('Total de partidas: '))
gols = int(input('Total de gols: '))
aproveitamento = gols/partidas 

jogador = {
    'nome': nome,
    'partidas': partidas,
    'gols': gols,
    'aproveitamento': aproveitamento
    }
print(jogador)
