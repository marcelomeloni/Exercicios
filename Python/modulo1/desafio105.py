'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e 
vai retornar um dicionário com as seguintes informações:


– Quantidade de notas                                                                                                                                                  
– A maior nota                                                                                                                                                                
– A menor nota                                                                                                                                                              
– A média da turma                                                                                                                                                      
– A situação (opcional)

'''
def notas():
    maior_nota = 0 
    c = 0
    menor_nota = 99999
    soma = 0
    while True:
        
        nota = float(input('Digite a nota do aluno: '))
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota 
        soma += nota
        c += 1
        opcao = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
        if opcao == 'N':
            break
    media = soma/c
    turma = {
        'maior_nota': maior_nota,
        'menor_nota': menor_nota,
        'media': media,
    }
    print(turma)
notas()
