#  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.



num = int(input("Digite um número para verificar se ele é primo, e se ele é par ou impar: "))

if num % 2 == 0:
    print("O número {} é par".format(num))
else:
    print("O número {} é impar".format(num))

primo = True
for x in range(2,num):
    if num % x == 0:
        primo = False
        break
print("{} é primo?: {}".format(num, primo))
