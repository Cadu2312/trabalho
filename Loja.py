#----Trabalho Final de Lógica de Programação----
#----Caso queira voltar ao Menu, digite 0----
fipe = {
    "c1":"March",
    "c2":"Corola",
    "c3":"Jeta",
    "c4":"Uno",
    "c5":"Agile",
    "c6":"Voyage",
    "c7":"Fusca",
    "c8":"C3",
    "c9":"HB20",
    "c10":"Onix"
}
fipe2 = {
    "c1":23000.0,
    "c2":40000.0,
    "c3":80000.0,
    "c4":15000.0,
    "c5":30000.0,
    "c6":25000.0,
    "c7":15000.0,
    "c8":40000.0,
    "c9":30000.0,
    "c10":25000.0
}
disponivel = {
    "c1":"Disponivel",
    "c2":"Disponivel",
    "c3":"Disponivel",
    "c4":"Disponivel",
    "c5":"Disponivel",
    "c6":"Disponivel",
    "c7":"Disponivel",
    "c8":"Disponivel",
    "c9":"Disponivel",
    "c10":"Disponivel"
}

cliente = {
    "nome":"",
    "saldo":0.0,
    "telefone":""
}

cliente["nome"] = input("Digite o nome do cliente: ")
cliente["saldo"] = input("Digite o saldo do cliente: ")
cliente["telefone"] = input("Digite o numero do cliente: ")
print("\n")


print("Programa aberto!")
sistema = 9

while sistema != 0:
    cont = 1
    print("\nAções disponvieis pelos clientes")
    print("1-Venda de veiculos")
    print("2-Aluguei de veiculos")
    print("3-Compra de veiculos")
    print("0-Finalizar programa\n")
    sistema = int(input("Digite a ação desejada: "))

    if sistema!=1 and sistema!=2 and sistema!=3 and sistema!=0:
        print("Ação inexistente")
    #Venda 
    if sistema == 1:
        print("12 porcento de desconto na venda! ")
        print("Carros que a empresa esta comprando")
        for i in fipe:
            o = fipe2[i]-(fipe2[i]*12)/100
            print(f"{fipe[i]}---> R${o} ")
        print("\n")
        vender = int(input("\n1-Escolher nome do carro quer deseja vender \n0-Voltar ao Menu\n"))
        if vender == 1:
            vender = str(input("Digite o nome do carro que o cliente deseja vender: "))
            cont = 1

            if cont != 0:
                for i in fipe:
                    x= vender in fipe[i]
                    if x == True:
                        break
                if x == False:
                    print("Carro não encontrado!\n")
                    cont = 0

        #Escolha do modelo que gostaria de vender
        if cont == 1:
            for i in fipe:
                if vender == fipe[i]:
                    print(f"Gostaria de relaxiar a venda do carro {fipe[i]} por R${fipe2[i]}")
                    aceitar = int(input("1-Sim \n2-Voltar ao Menu \n"))
                    #Caso aceite vender
                    if aceitar == 1:
                        print("\nCarro Vendido!")
                        cliente["saldo"] = float(cliente["saldo"]) + float(fipe2[i])
                        print(f'Cliente: {cliente["nome"]} \nSaldo: {cliente["saldo"]} \nTelefone: {cliente["telefone"]}')
                        disponivel[i] = "Disponivel"
                    if aceitar != 1:
                        continue
        #Alugar carro
    if sistema == 2:
        #Carros Disponiveis
        for i in fipe:
            if disponivel[i] == "Disponivel":
                print(f"{fipe[i]} ---- {disponivel[i]}")
        alugar = int(input("1-Alugar carro \n0-Voltar ao Menu \n"))
        if alugar == 1:
            alugar = str(input("Qual carro gostaria de alugar: "))
            dias = int(input("Quantos dias de aluguel: "))
            aluguelpreco = 77 * dias
            print(f"\nO valor ficara em {aluguelpreco}.")
            cont = int(input("\n1-Alugar carro escolhido \n0-Voltar ao Menu"))

            if cont != 0:
                for i in fipe:
                    x= alugar in fipe[i]
                    if x == True:
                        break
                if x == False:
                    print("Carro não encontrado!\n")
                    cont = 0


            if cont == 1:
                for i in fipe:
                    if alugar == fipe[i] and disponivel[i] == "Disponivel":
                        if float(cliente["saldo"]) >= aluguelpreco:
                            cliente["saldo"] = float(cliente["saldo"]) - aluguelpreco
                            disponivel[i] = "Indisponivel"
                            print("\nCarro alugado")
                            print(f'Cliente: {cliente["nome"]} \nSaldo: {cliente["saldo"]} \nTelefone: {cliente["telefone"]}')
                        if float(cliente["saldo"]) < aluguelpreco:
                            print("\nSaldo indisponivel")
                            print(f'Cliente: {cliente["nome"]} \nSaldo: {cliente["saldo"]} \nTelefone: {cliente["telefone"]}')
    #Comprar carro
    if sistema == 3:
        print("Carros disponvieis esta comprando")
        for i in fipe:
            if disponivel[i] == "Disponivel":
                o = fipe2[i]+(fipe2[i]*25)/100
                print(f"{fipe[i]}---> R${o} ")
        comprar = int(input("1-Comprar carro \n0-Voltar ao Menu \n"))
        if comprar == 1:
            comprar = str(input("Qual carro gostaria de comprar: "))
            cont = int(input("\n1-Comprar carro escolhido \n0-Voltar ao Menu"))

            if cont != 0:
                for i in fipe:
                    x= comprar in fipe[i]
                    if x == True:
                        break
                if x == False:
                    print("Carro não encontrado!\n")
                    cont = 0


            if cont == 1:
                for i in fipe:
                    if comprar == fipe[i] and disponivel[i] == "Disponivel":
                        if float(cliente["saldo"]) >= float(fipe2[i]):
                            cliente["saldo"] = float(cliente["saldo"]) - float(fipe2[i])
                            disponivel[i] = "Indisponivel"
                            print("\nCarro Comprado")
                            print(f'Cliente: {cliente["nome"]} \nSaldo: {cliente["saldo"]} \nTelefone: {cliente["telefone"]}')
                        if float(cliente["saldo"]) < float(fipe2[i]):
                            print("\nSaldo indisponivel")
                            print(f'Cliente: {cliente["nome"]} \nSaldo: {cliente["saldo"]} \nTelefone: {cliente["telefone"]}')


            
