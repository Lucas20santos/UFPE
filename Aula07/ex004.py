from os import system as linux
linux("clear")

listaNumeros = []


while True:
    listaNumeros.append(float(input("Digite um número: ")))
    if listaNumeros[len(listaNumeros) - 1] == 0:
        break

listaNumeros.pop()
print(f"Os números informados foram:: {listaNumeros}")
