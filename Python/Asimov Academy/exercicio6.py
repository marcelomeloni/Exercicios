'''
Você fez uma pequena pesquisa de preferência entre três produtos A, B e C. 
Na entrevista, cada entrevistado precisava escolher seu produto preferido. 
Os votos obtidos nessa pesquisa estão representados na lista abaixo:

votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]
Testar
Agora, seu objetivo é calcular qual produto foi o mais votado. 
A partir da lista de votos, crie um dicionário onde a chave é cada produto, e o valor é o número de votos que o produto recebeu.
'''

votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]
qntvotosA = qntvotosB = qntvotosC = 0
for c in votos:
    if c == "A":
        qntvotosA += 1
    elif c == "B":
        qntvotosB += 1 
    else:
        qntvotosC += 1

resultado = {
    "Produto A": qntvotosA,
    "Produto B": qntvotosB,
    "Produto C": qntvotosC
}
print(resultado)
