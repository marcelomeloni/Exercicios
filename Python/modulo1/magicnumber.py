import random
magicnum = random.randint(1,100)
num = int(input("Digite um número: "))
while num != magicnum:
    if num < magicnum:
        print("O número mágico é maior!")
    else:
        print("O número mágico é menor!")
    if num != magicnum:
        num = int(input("Você errou tente novamente: "))
print("Parabéns! Você ganhou!")
    
