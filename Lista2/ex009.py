"""Crie duas listas com números de 0 a 9, embaralhe as listas e sorteie um número de cada
uma para formar uma dezena, repita a operação 5 vezes para sortear 5 dezenas, assim
como na mega sena. Caso a dezena caia como 00 (zero, zero) faça o sorteio dela
novamente até sair outra combinação. Depois disso exiba as dezenas sorteadas.
"""
from packages.organizar import limpar
limpar()
from random import shuffle, randint


lista1 = list(range(0, 10))
lista2 = list(range(0, 10))
shuffle(lista1)
shuffle(lista2)


megaSena = []

while True:
    pos1 = randint(0, 9)
    pos2 = randint(0, 9)
    if pos1 == 0 and pos2 == 0:
        continue
    num = str(lista1[pos1]) + str(lista2[pos2])
    megaSena.append(num)

    if len(megaSena) == 5:
        break

print(f"Os números da mega sena são: {megaSena}")
