#  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input("Digite um número para verificar se ele é primo: "))
primo = True
for x in range(2,num):
    if num % x == 0:
        primo = False
        break
print("{} é primo?: {}".format(num, primo))
