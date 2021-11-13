"""Usando dicionário, faça um programa que represente uma jogada de um dado
entre 5 jogadores (imprima na tela o valor que cada jogador tirou no dado). Os
resultados são aleatórios, logo, para cada jogada teremos valores diferentes.
Em seguida, exiba a ordem de cada jogador (lembrando que o primeiro lugar
será o jogador que tirou o maior número no dado).

Obs: use as funções randint, sleep e itemgetter referente aos pacotes random,
time operator respectivamente"""
from random import randint
from os import system as linux
from time import sleep
from operator import itemgetter

linux("clear")

jogadasJogadores = {
    "Jogador1": 0,
    "Jogador2": 0,
    "Jogador3": 0,
    "Jogador4": 0,
    "Jogador5": 0
}

for i in range(5):
    print(f"{i + 1}º jogada sendo feita...")
    jogadasJogadores["Jogador"+str(i + 1)] = randint(1, 6)
    sleep(2)
    print(f"{i + 1}º jogada foi concluída!")
    sleep(1)
    linux("clear")

print("Jogadas: ", jogadasJogadores)

jogadoresOrdenados = dict(sorted(jogadasJogadores.items() ,key=itemgetter(1), reverse=True))
print(jogadoresOrdenados)
