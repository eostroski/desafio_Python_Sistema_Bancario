menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if (valor_deposito>0):
            print(f"o valor de R$:{valor_deposito:.2f} foi depositado na sua conta!")
            saldo += valor_deposito
            extrato += f"Depósito de {valor_deposito:.2f}\n"
        else:
            print("***** O valor deve ser maior que 0 *****")
            
            
    elif opcao == "s":
        print("Saque")
        valor_saque =  float(input("Digite o valor a ser sacado: "))

        if(valor_saque>saldo):
            print("Saldo insuficiente!")

        elif(valor_saque>limite):
            print(f"O limite por saque é de R$:{limite:.2f}")

        elif(numero_saques>=LIMITE_SAQUES):
            print("Número de saques excedido")

        elif (valor_saque>0):
            print(f"o valor de R$:{valor_saque:,.2f} foi sacado da sua conta!")
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque de {valor_saque:.2f}\n"
        else:
            print("***** O valor deve ser maior que 0 *****")
            
    elif opcao == "e":
        print(f"Extrato:\n{extrato}\n")
        print(f"Seu saldo é de {saldo:.2f}")
        

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")
