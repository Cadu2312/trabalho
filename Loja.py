#----Trabalho Final de Lógica de Programação----
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

cliente = {
    "nome":"",
    "saldo":0.0,
    "telefone":""
}

cliente["nome"] = input("Digite o nome do cliente: ")
cliente["saldo"] = input("Digite o saldo do cliente: ")
cliente["telefone"] = input("Digite o numero do cliente: ")
print("\n")


print("Programa aberto!\n")
sistema = 9

while sistema != 0:
    cont = 1
    print("Ações disponvieis pelos clientes")
    print("1-Venda de veiculos")
    print("2-Aluguei de veiculos")
    print("3-Compra de veiculos")
    print("0-Finalizar programa\n")
    sistema = int(input("Digite a ação desejada: "))

    if sistema!=1 and sistema!=2 and sistema!=3 and sistema!=0:
        print("Ação inexistente")
    if sistema == 1:
        print("12 porcento de desconto na venda! ")
        print("Carros que a empresa esta comprando")
        for i in fipe:
            o = fipe2[i]-(fipe2[i]*12)/100
            print(f"{fipe[i]}---> R${o} ")
        print("\n")
        vender = str(input("Digite o nome do carro que o cliente deseja vender: "))
        for i in fipe:
            if vender == fipe[i]:
                print(f"Gostaria de relaxiar a venda do carro {fipe[i]} por R${fipe2[i]}")
                aceitar = int(input("1-Sim \n2-Não"))
                if aceitar == 1:
                    print("\nCarro Vendido!")
                    cliente["saldo"] = cliente["saldo"] + fipe2[i]
                    print(f"Cliente: {cliente["nome"]} \nSaldo: {cliente["saldo"]} \nTelefone: {cliente["telefone"]}")
