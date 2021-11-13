from os import system as linux
linux("clear")

listaNumeros = [7, 7, 27, 39, 100]

numeroParaSerEncontrado = int(input("Digite o número que você deseja encontrar:: "))

print("Primeira IF-ELSE")
print(30 *"=")
if numeroParaSerEncontrado in listaNumeros:
    ## Maneira 1
    print(30 *"=")
    for x in range(0, len(listaNumeros)):
        if numeroParaSerEncontrado == listaNumeros[x]:
            print(f"O número {numeroParaSerEncontrado} foi encontrado na posição {x + 1}")

    print(30 *"=")
    ## Meneira 2
    for k, v in  enumerate(listaNumeros):
        if v == numeroParaSerEncontrado:
            print(f"O valor {numeroParaSerEncontrado} foi encontrado na posição {k + 1}")
    
    print(30 *"=")
    ## Maneira 3
    for k, v in enumerate(listaNumeros):
        if v is numeroParaSerEncontrado:
            print(f"O valor {numeroParaSerEncontrado} foi encontrado na posição {k + 1}")
    
    print(30 *"=")
    ## Maneira 4
    for k, v in enumerate(listaNumeros):
        if v is not numeroParaSerEncontrado:
            continue
        else:
            print(f"O valor {numeroParaSerEncontrado} foi encontrado na posição {k + 1}")
else:
    print("O numero não foi encontrado na lista")


print()
print("Segundo IF-ELSE")
print(30 *"=")
if numeroParaSerEncontrado not in listaNumeros:
    print("O numero não foi encontrado na lista")
else:
    print(30 *"=")
    ## Maneira 1
    for x in range(0, len(listaNumeros)):
        if numeroParaSerEncontrado == listaNumeros[x]:
            print(f"O número {numeroParaSerEncontrado} foi encontrado na posição {x + 1}")
    
    print(30 *"=")
    ## Meneira 2
    for k, v in  enumerate(listaNumeros):
        if v == numeroParaSerEncontrado:
            print(f"O valor {numeroParaSerEncontrado} foi encontrado na posição {k + 1}")
    
    print(30 *"=")
    ## Maneira 3
    for k, v in enumerate(listaNumeros):
        if v is numeroParaSerEncontrado:
            print(f"O valor {numeroParaSerEncontrado} foi encontrado na posição {k + 1}")
    
    print(30 *"=")
    ## Maneira 4
    for k, v in enumerate(listaNumeros):
        pos = 0
        if v is not numeroParaSerEncontrado:
            continue
        else:
            print(f"O valor {numeroParaSerEncontrado} foi encontrado na posição {k + 1}")

