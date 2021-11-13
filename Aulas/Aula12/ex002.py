from functools import reduce
from os import system as linux
linux("clear")

nomeJogador = input("Nome do jogador: ")
quantidadePartidas = int(input("Informe a quantidade de partidas: "))
quantidadeGolCadaPartida = []
for i in range(0, quantidadePartidas):
    quantidadeGolCadaPartida.append(int(input(f"Quantidade de gol feito na partida {i + 1}: ")))

# A função reduce recebe dois parâmetros... o primeiro uma função e o outro uma sequência
quantidadeTotalGol = reduce(lambda x, y: x + y , quantidadeGolCadaPartida)
print(f"O jogador, {nomeJogador}, marcou {quantidadeTotalGol} Gols!")
