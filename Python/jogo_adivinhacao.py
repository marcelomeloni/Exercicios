'''
Desenvolva um jogo de acerte o número, onde o computador escolhe um número inteiro aleatório de 0 a 10, e o usuário tem 
5 tentativas para adivinhar o número

OBS.: O design da tela pode ser implementado livremente

(PLUS): Implemente um sistema de pontuação com o seguinte comportamento: se o usuário adivinhar o número na primeira tentativa, 
receberá a pontuação máxima (ex. 100 pontos); se o usuário adivinhar o número na última tentativa, receberá a pontuação mínima
(ex. 10 pontos); se o usuário não acertar o número, não receberá nenhum ponto.

(PLUS): Implemente um controle de erros. Caso o jogador digite um número fora da faixa permitida ou caracteres não numéricos, 
o sistema deve notificar o jogador e solicitar o input correto.

(PLUS): Implemente a opção de o usuário iniciar uma nova partida. Ao finalizar uma rodada, após o resultado final, 
o jogo deve perguntar se o jogador quer iniciar uma nova partida e, em caso negativo, encerrar a aplicação.
'''
import random
ativo = True

vitorias = 0 
total_pontos = 0 
maior_pontuacao = 0 
partidas_jogadas = 0 
primeira = 0 
ultima = 0

while True:
    if ativo:
        while True:
            novaPartida = str(input("Deseja iniciar uma nova partida? [Sim/Não] ")).upper().strip()
            if novaPartida == 'S':
                numero_magico = random.randint(0,10)
                c = 0
                acertou = False
                pontos = 0
                partidas_jogadas += 1
                while c < 5:
                    #Nova Partida
                    
                    print("Pensei em um número, sera que você consegue adivinhar?")
                    numero_escolhido = int(input("Digite um número de 0 a 10!"))
                    if numero_escolhido < 0:
                        print("Digite um número maior que 0!")
                        numero_escolhido = int(input("Digite um número de 0 a 10!"))
                    elif numero_escolhido > 10:
                        print("Digite um número menor que 10!")
                        numero_escolhido = int(input("Digite um número de 0 a 10!"))
                    else:
                        if numero_escolhido == numero_magico:
                            acertou = True
                            print("Você ganhou!")
                            c += 1
                            if c == 1:
                                print('Que sorte! Ganhou na primeira tentativa.')
                                primeira += 1
                                
                            elif c == 5:
                                print('Quase eim! Ganhou na ultima...')
                                ultima += 1
                            else:
                                print(f'Você ganhou com {c} tentativas!')
                                
                            pontos = 100 - (20*(c-1))
                            vitorias += 1
                            total_pontos += pontos
                            if pontos > maior_pontuacao:
                                maior_pontuacao = pontos
                                
                            print(f'Pontos ganhos: {pontos}')
                          
                            break
                        elif numero_escolhido < numero_magico:
                            print("Digite um número maior!")
                            c += 1
                        elif numero_escolhido > numero_magico:
                            print("Digite um número menor!")
                            c += 1
                if not acertou:
                    print(f"Que pena, você esgotou as 5 tentativas. O número era {numero_magico}.")
             
                
                
                
                
          
                
                
                
            elif novaPartida == 'N':
                estatisticas = str(input("Deseja Visualizar as estatisticas? [Sim/Não]")).upper().strip()
                if estatisticas == 'S':
                    print('-='*20)
                    print(f'Quantidade de vitorias: {vitorias}')
                    print(f'Quantidade total de pontos: {total_pontos}')
                    print(f'Maior quantia de pontos em uma partida: {maior_pontuacao}')
                    print(f'Partidas jogadas: {partidas_jogadas}')
                    print(f'Porcentagem de vitoria: {vitorias*100/partidas_jogadas}%')
                    print(f'Quantas vezes ganhou na 1° rodada: {primeira}')
                    print(f'Quantas vezes ganhou na ultima rodada: {ultima}')
                    print('-='*20)
                else:
                    fecharJogo = str(input("Deseja sair do jogo? [Sim/Não]")).upper().strip()
                    if fecharJogo == 'S':
                        ativo = False
                        break
            else:
                print('Resposta Invalida. Digite sim ou não.')
            
    else:
        break
