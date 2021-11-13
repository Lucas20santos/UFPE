"""Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba
os valores mês a mês para os 24 primeiros meses.▪Escreva um programa que pergunte o depósito
inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
"""

depositoInicial = float(input("Deposito Inicial: "))
taxaJurosPoupanca = float(input("Taxa de Juros:: "))
montanteMesAMes = 0


for t in range(0, 25):
    montanteMesAMes = round(depositoInicial * (1 + taxaJurosPoupanca / 100) ** t, 3)
    print(f"Mes {t} - deposito inicial {depositoInicial} - juros {round(montanteMesAMes - depositoInicial, 3)} - montante mes a mes {montanteMesAMes}")
