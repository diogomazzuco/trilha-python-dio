from time import sleep
print("\n------- SEJA BEM VINDO AO BANCO FERREIRA -------")
sleep(1)
menu = """\n
Digite a opção desejada

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        print("Deposito")
        valor = float(input("Digite o valor a ser depositado: "))
        extrato += f"Deposito: R$ {valor:.2f} \n"
        
        if valor > 0:
            saldo += valor
        else:
            print("Falha na operação! O valor digitado é invalido!")

    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques > LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Falha na Operação! Você não tem saldo suficiente. ")
        
        elif excedeu_limite:
            print("Falha na Operação! Você excedeu o valor permitido de saque de R$ 500.00")
            
        elif excedeu_saques:
            print("Falha na Operação! Você atingiu o número de saques permitidos ")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f} \n"
            numero_saques += 1
        
        else:
            print("Falha na operação! O valor digitado é invalido!")
                
        
    elif opcao == "3":
        print("########## Extrato ##########\n")
        print("Você ainda não realizou movimentações." if not extrato else extrato)
        print(f"\nO seu saldo é de: R$ {saldo:.2f}")
        print(30 * "#")
        
        
    elif opcao == "0":
        print("Obrigado por utlizar nossos serviços! Volte sempre!")
        break
        
    else:
        print("Opção Invalida, por favor selecione novamente a opção desejada")
