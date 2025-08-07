# Exercício de Python 3: quem gastou mais dinheiro?

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]
soma_j = 0
soma_p = 0
for gastosj in gastos_joao:
    soma_j += gastosj
for gastosp in gastos_pedro:
    soma_p += gastosp
if (soma_j > soma_p):
    print("João gastou mais dinheiro")
elif (soma_p > soma_j):
    print("Pedro gastou mais dinheiro")
else:
    print("Os gastos foram iguais")
   
