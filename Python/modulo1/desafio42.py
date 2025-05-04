# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:



print("Para analisar o triangulo, digite seus segmentos.")
a = int(input("Primeiro segmento:"))
b = int(input("Segundo segmento: "))
c = int(input("Terceiro segmento: "))
if a == b and a == c:
	tipo = "equilatero"
if a == b and b != c:
	tipo = "isosceles"
if c == a and c != b:
	tipo = "isosceles"
if c == b and c != a:
	tipo = "isosceles"
if a !=b and c !=a and c != b:
	tipo = "escaleno"
if a < (c+b) and b < (a+b) and c < (b+a):
	print("O triangulo existe! E é do tipo {}".format(tipo))
else:
	print("O triangulo nao existe!")
