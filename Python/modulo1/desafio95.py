'''

Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

jogador = dict()
jogadores = list()
while True:
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
    jogadores.append(jogador.copy())

    
    opcao = str(input('Você deseja continuar? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
while True:
    busca = str(input('Faça a busca do nome de um jogador para exibir detalhes: [DIGITE FIM PARA SAIR] '))
    if busca == 'FIM':
        break 
    for c in range(0,len(jogadores)):
        if busca == jogadores[c]['nome']:
            for v,k in jogador.items():
                print(f'{v}: {k}')
