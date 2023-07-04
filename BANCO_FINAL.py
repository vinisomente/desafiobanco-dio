import time

print ('-=-'*11)
print('''
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair
''')
print ('-=-'*11)

saldo = 0
extrato = ''
limite_saque = 3
limite_valor = 500

while True:
    opcao = input ('O que você deseja fazer?\n')
    if opcao == '0':
        time.sleep(0.3)
        print ('Você solicitou um depósito.', end=' ')
        deposito = float(input('Qual o valor que você deseja depositar? R$  '))

        if deposito <= 0:
            print ('Este não é um valor válido.')
            print('-=-' * 11)

        else:
            saldo += deposito
            extrato += f'Depósito: R${deposito:.2f}\n'
            print (f'Você depositou R${deposito:.2f} em sua conta, agora possui R${saldo:.2f}.')
            print('-=-' * 11)

    elif opcao == '1':
        time.sleep(0.3)
        print ('Você solicitou um saque.', end=' ')
        saque = float (input('Qual o valor que você deseja sacar? R$ '))

        if saque > saldo:
            print ('Não há saldo suficiente em sua conta, você não poderá realizar a operação.')
            print('-=-' * 11)

        elif limite_saque <= 0:
            print ('Você excedeu o seu limite de saque diário. A operação não poderá ser realizada')
            print('-=-' * 11)

        elif saque > limite_valor:
            print ('Você ultrapassou o limite de R$ 500.00 do saque. A operação não poderá ser realizada.')
            print('-=-' * 11)

        elif saque <= 0:
            print ('Este não é um valor válido. A operação não poderá ser realizada')
            print('-=-' * 11)
        else:
            limite_saque -= 1
            saldo -= saque
            extrato += f'Saque: R${saque:.2f}\n'
            print (f'Você realizou o saque de R${saque:.2f} e agora possui R${saldo:.2f} em sua conta')
            print('-=-' * 11)

    elif opcao == '2':
        time.sleep(0.3)
        print ('-='*11,'EXTRATO','-='*11)
        print ('Não foram realizadas movimentações.' if not extrato else extrato)
        print (f'Saldo: R${saldo:.2f}')
        print ('-=-'*18)


    elif opcao == '3':
        print ('O programa será encerrado, volte sempre!')
        break

    else:
        print ('Isso não é uma opção válida.')
        print ('-=-' * 11)