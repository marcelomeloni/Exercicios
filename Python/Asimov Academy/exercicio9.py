'''
Você está recebendo muitos emails de spam na sua empresa. 
Para bloqueá-los, você deseja criar um script em Python capaz de detectar um email de spam a partir do seu domínio 
(o nome após o sinal de @).

Crie uma função em Python para implementar essa funcionalidade. 
A função deve exibir uma mensagem de acordo com o e-mail ser spam ou não. 
Para o exercício, considere que e-mails enviados do domínio @xyz.com são mensagens de spam
'''

email = str(input("Digite seu email: "))

if ("@" in email):
    if ("@xyz.com" in email):
        print("Email considerado spam")
    else:
        print('Mensagem enviada com sucesso!')
else:
    print("Digite um email valido (com @)")
