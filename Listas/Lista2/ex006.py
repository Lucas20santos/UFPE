"""
Faça um programa que exiba uma lista formada pelos X primeiros números primos de
uma dada lista. A lista dos números primos deverá ser originada, através de uma lista
formada por números inteiros de 1 até 200. A ideia é deixar que o usuário defina o
número X (quantidade de números primos).
"""
from packages.organizar import limpar, criarLinha
from packages.lista import exibir, criaLista

limpar()
lista = list(range(10))

criarLinha(90, "=", texto=" Aula 06 ")
exibir(texto="Essa é minha lista: ", lista=lista)
criarLinha(90, "=", texto=" Lista de 0 à 200 elementos ")

lista = criaLista(201)
print(lista)
criarLinha(90, "=", texto=" Informe um número X ")

while True:
    try:
        x = int(input("Informe um número inteiro: "))
    except:
        print("Infome um valor válido!")
    else:
        break
print("valor de x = ",x)
listaNumPrimo = []
cont = 0

while len(listaNumPrimo) < x:
    for i in lista:
        if i == 0 or i == 1:
            continue
        for j in range(1, i + 1):
            if i % j == 0:
                cont += 1
        if cont == 2:
            listaNumPrimo.append(i)
        cont = 0

exibir(f"Lista números primos até ", listaNumPrimo[:x])
criarLinha()
