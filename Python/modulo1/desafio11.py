# quantidade de tinta necessaria para pintar determinada area ( 1 lata = 2 m^2)

l = float(input('Qual a largura da parede? (em metros): '))
h = float(input('Qual a altura da parede? (em metros): '))

a = l*h

print('Serão necessarias {} latas de tinta para pintar a parede!'.format(a/2))
