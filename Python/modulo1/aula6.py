#Verificação do erro, somar strings

n1 = (input('Digite um valor: '))
n2 = (input('Digite outro valor: '))
soma = n1 + n2
print('A soma de', n1 , "e", n2 , "é:",soma)


#verificar tipo de variavel n1, esperado tipo str
n1 = input('Digite um valor: ')
print(type(n1))

#verificar tipo de variavel de n1, esperado tipo int

n1 = int(input('Digite um valor: '))
print(type(n1))

n2 = int(input('Digite outro valor: '))

soma = n1 + n2

#sem {}
print('A soma de', n1 , "e", n2 , "é:",soma)

#com {}
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
