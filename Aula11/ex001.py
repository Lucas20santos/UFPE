"""
Faça um programa usando dicionário que mostre o preço de um determinado produto  definido 
pelo usuário. (Ex.: dicionário com os modelos de carros e o respectivo valor de cada um 
deles)
"""
from os import system as linux
linux("clear")

carros = {"produtos": [], "precos": []}

while True:
    carros["produtos"].append(input("Informe o nome do carro: "))
    carros["precos"].append(float(input("informe o preço do produto: ")))

    opcao = input("Deseja inserir mais produtos!\n-> S/s - Sim ou N/n - Não: ").strip()[0].upper()
    while opcao not in "SnNs":
        opcao = input("Erro!\n-> Digite S/s - Sim ou N/n - Não: ")
    
    if opcao in "Nn":
        break

print(carros)
