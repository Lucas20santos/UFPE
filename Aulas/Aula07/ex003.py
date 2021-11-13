from os import system as linux
linux("clear")

depositoInicial = float(input("Deposito Inicial: "))
taxaJurosPoupanca = float(input("Taxa de Juros:: "))
montanteMesAMes = 0


for t in range(0, 25):
    montanteMesAMes = round(depositoInicial * (1 + taxaJurosPoupanca / 100) ** t, 3)
    print(f"Mes {t} - deposito inicial {depositoInicial} - juros {round(montanteMesAMes - depositoInicial, 3)} - montante mes a mes {montanteMesAMes}")
