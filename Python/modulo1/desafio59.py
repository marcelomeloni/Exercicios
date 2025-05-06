opcao = 0

while opcao != 5:
    num1 = float(input('Digite um valor: '))
    num2 = float(input('Digite outro valor: '))
    
    while True:
        print('-='*10)
        print('MENU DE OPÇÕES')
        print('-='*10)
        print(''' [ 1 ] somar
[ 2 ] multiplicar 
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa ''')
        opcao = int(input('Digite sua opção: '))
        
        if opcao == 1:
            resposta = num1 + num2
            print(f'A soma é {resposta}')
        elif opcao == 2:
            resposta = num1 * num2
            print(f'O produto é {resposta}')
        elif opcao == 3:
            resposta = max(num1, num2)
            print(f'O maior valor é {resposta}')
        elif opcao == 4:
            break  # Sai do menu interno e pede novos números
        elif opcao == 5:
            print('Finalizando o programa...')
            break
        else:
            print('Opção inválida! Tente novamente.')
    
    if opcao == 5:
        break

print('Programa encerrado.')
