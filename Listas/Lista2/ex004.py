"""Escreva um programa que carregue uma lista com os modelos de dez carros (Fusca, Gol,
Celta, Uno, etc) e outra lista com o consumo de cada modelo (km/litro). Por fim, exiba:
a. O modelo do carro mais econômico.
b. Quantos litros cada modelo de carro cadastrado consome para percorrer uma
distância de X km.
c. Quanto será gasto de combustível para percorrer X km, considerando que a
gasolina custe R$ 5,50 o litro.
"""
from os import system as linux
linux("clear")

def insereLinhaBonita(texto):
    print(f" {texto} ".center(70, "="))

modeloCarro = ['BMW', "Chevrolet Celta 2015", "Citroen Bx", "Dodge 1800", "Ferrari California 2017"
, "Palio Attractive 1.0", "Ford Belina 1991", "Honda City 2018",
"Hummer H3 2010", "Hyundai Azera 2017"]

KmPorLitro = [8.4, 7.6, 8.5, 8, 5.8, 7.2, 6.3, 8.6, 4.3, 7]

consumoPorKm = list(map(lambda x: round(1/ x, 2), KmPorLitro))

menorConsumo = 0
posicao = 0

insereLinhaBonita("Letra A")
print(f"Lista de consumo dos carros:\n{consumoPorKm}")
for k, v in enumerate(consumoPorKm):
    if k == 0:
        menorConsumo = round(v, 4)
        posicao = k
    else:
        if v < menorConsumo:
            menorConsumo = round(v, 4)
            posicao = k

print(f"O carro que tem menor consumo por litro é: {modeloCarro[posicao]}")

insereLinhaBonita("Letra B")
km = float(input("Informe a quantidade de KM: "))

consumoPorMaisDeKm = list(map(lambda x: round(km * x, 2), consumoPorKm))
print(f"Em {km} Km percorridos:\nConsumo: {consumoPorMaisDeKm}")

insereLinhaBonita("Letra C")
preco = 5.5
gasto = list(map(lambda x: round(x * preco, 2), consumoPorMaisDeKm))
print(f"O gasto que o usuário vai ter é:\n{gasto}")
insereLinhaBonita("")
