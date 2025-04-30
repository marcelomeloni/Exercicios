nome_completo = input("Digite seu nome completo: ")

print(nome_completo.upper())
print(nome_completo.lower())

dividido = nome_completo.split()

# Soma a quantidade de letras de todas as partes do nome (sem contar espaços)
qntletras = sum(len(parte) for parte in dividido)

print('Quantidade de letras do nome todo: {}'.format(qntletras))
print('Quantidade de letras do primeiro nome: {}'.format(len(dividido[0])))
