"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e quantidade de anos a
pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o
valor da prestação como sendo o valor da casa a comprar dividido pelo número de
meses a pagar.
"""
from os import system as linux
linux("clear")

while True:
    print("Valor do apartamento: ")
    while True:
        try:
            valorDaCasa = float(input("Informe o valor do apartamento: "))
        except:
            linux("clear")
            continue
        else:
            break

    linux("clear")
    
    # Salário
    print("Salário: ")
    while True:
        try:
            salario = float(input("Informe o valor do seu salário: "))
        except:
            linux("clear")
            print("Valor informado invalido! Informe um valor válido: ")
        else:
            break

    linux("clear")

    # Tempo do financiamento
    print("Tempo do financiamento: ")
    while True:
        try:
            quantidadeAnos = int(input("Informe o tempo de financiamento em anos: "))
        except:
            linux("clear")
            print("Valor informado invalido! Informe um valor válido: ")
        else:
            break

    linux("clear")

    print("""
    Formula matemática para calcular a parcela
    PMT = PV { i ( 1 + i )^n / [ ( 1 + i )^n -1 }
    onde, 
    PMT -> valor da parcela mensalmente,
    PV  -> valor principal ou valor a vista do imovel,
    i   -> taxa de juros por ano,
    n   -> tempo em anos
    """
    )
    taxaJuros = 0.03

    # calculo das parcelas
    PMT = valorDaCasa * ((taxaJuros * (taxaJuros + 1)** quantidadeAnos) / ((1 + taxaJuros) ** quantidadeAnos - 1))

    if PMT > salario * 0.3:
        print(f"Valor das Parcelas: {round(PMT, 3)}")
        print(f"30% do seu salárivo equivale a: {salario * 0.3}")
        print("O tempo informado foi insuciente para efetuar a compra!")
    else:
        print(f"Valor das Parcelas: {round(PMT, 3)}")
        print(f"30% do seu salárivo equivale a: {salario * 0.3}")
        print("O tempo é suficiente para um financiamento. Agora digite n[não] para prosseguir com o seu financiamento.")
    
    opcao = input("Deseja continuar!S[sim] - N[não]").upper().strip()[0]

    while True:
        if opcao not in "NSns":
            print ("valor informado invalido!")
            opcao = input("Deseja continuar!S[sim] - N[não]").upper().strip()[0]
        else:
            break
    linux("clear")

    if opcao == "N":
        break    

print("Final do programa!")
