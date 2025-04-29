#Verificar tipo premitivo e outras informações de entrada

entrada = input('Digite algo: ')

print(type(entrada))

upper = entrada.isupper()
print('Você digitou algo em letras maisculas? {}'.format(upper))

lower = entrada.islower()
print('Você digitou algo em letras minusculas? {}'.format(lower))

numeric = entrada.isnumeric()
print('Você digitou algo somente com numeros? {}'.format(numeric))

alpha = entrada.isalpha()
print('Você digitou algo somente com letras? {}'.format(alpha))

alnum = entrada.isalnum()
print('Você digitou algo em alphanumerico? {}'.format(alnum))
