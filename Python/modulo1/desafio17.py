import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

hip = math.trunc(math.sqrt(pow(ca, 2) + pow(co, 2)))

print('A hipotenusa é', hip)
