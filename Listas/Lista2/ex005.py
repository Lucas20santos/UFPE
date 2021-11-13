"""
Faça um Programa que leia duas listas com 15 elementos cada e gere uma terceira
lista formada pelos elementos intercalados das duas outras listas. O programa deve
exibir a quantidade de elementos de cada lista, bem como seus elementos.
"""
from os import system as linux
linux("clear")


def criarLinha():
    print(" ".center(70, "="))


lista1 = []
lista2 = []
lista3 = []
criarLinha()
print("INSERINDO ELEMENTOS NAS LISTAS".center(70, " "))
criarLinha()

for i in range(2):
    while True:
        try:
            lista1.append(int(input(f"informe o {i + 1}º elemento da lista 1: ")))
        except:
            print("Informe um número inteiro valido!")
        else:
            break
    
    while True:
        try:
            lista2.append(int(input(f"informe o {i + 1}º elemento da lista 2: ")))
        except:
            print("Informe um número inteiro valido!")
        else:
            break

print(f"A lista 1 contém esses elementos: {lista1}")
print(f"A lista 2 contém esses elementos: {lista2}")

criarLinha()
print("GERANDO UMA TERCEIRA LISTA".center(70, " "))
criarLinha()

for i in range(len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(f"A lista 3 foi criada com esses elemetnos: {lista3}")
print(f"A lista 1 tem {len(lista1)} elementos")
print(f"A lista 2 tem {len(lista2)} elementos")
print(f"A lista 3 tem {len(lista3)} elementos")
criarLinha()
