# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

city = input('Digite o nome da cidade: ').strip().lower()
print(city.startswith('santo'))
