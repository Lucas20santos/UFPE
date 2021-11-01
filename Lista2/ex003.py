"""
Escreva um programa que solicite ao usuário 10 valores (1 até 10) e guarde-os em uma
tupla. O programa deverá realizar uma análise dos valores inseridos e exibir:
a. Quantas vezes o número 5 foi digitado;
b. Qual a posição do número 3;
c. Quantos números pares e ímpares foram digitados, informe quais foram.
"""
from os import system as linux
linux("clear")

def printarLinha():
    print(40 * "-")


def verificaNumeroCinco(tupla):
    cont = 0
    for v in tupla:
        if v == 5:
            cont += 1
    if cont == 1:
        print(f"O número 5 apareceu {cont} vez!")
    elif cont > 1:
        print(f"O número 5 apareceu {cont} vezes!")
    else:
        print(f"O número 5 não apareceu nos números digitados!")


def verificaNumeroTres(tupla):
    posicoes = []
    for k, v in enumerate(tupla):
        if v == 3:
            posicoes.append(k + 1)
    if len(posicoes) == 1:
        print(f"O valor 3 apareceu na posição {posicoes}!")
    elif len(posicoes) > 1:
        print(f"O valor 3 apareceu nas posições {posicoes}!")
    else:
        print("O número 3 não foi digitado!")


def varificaNumerosParesImpares(tupla):
    numPar = 0
    numImpar = 0
    bibliotecaDeNumero = {"numeroPares":[], "numeroImpares": []}
    
    for v in tupla:
        if v % 2 == 0:
            numPar += 1
            bibliotecaDeNumero["numeroPares"].append(v)
        else:
            numImpar += 1
            bibliotecaDeNumero["numeroImpares"].append(v)
    print(f"Foi digitados {numPar} pares - Números Pares: {bibliotecaDeNumero['numeroPares']}")
    print(f"Foi digitados {numImpar} impares - Números Impares: {bibliotecaDeNumero['numeroImpares']}")


tuplaDeNumero = ()
    
printarLinha()
print("Informe 10 números na tupla ".center(40))
printarLinha()

for i in range(10):
    while True:
        try:
            num = float(input(f"Informe o {i + 1}º número: "))
            tuplaDeNumero += (num,)
        except:
            print("Digite um valor válido")
        else:
            break

printarLinha()
verificaNumeroCinco(tuplaDeNumero)

printarLinha()
verificaNumeroTres(tuplaDeNumero)

printarLinha()
varificaNumerosParesImpares(tuplaDeNumero)
printarLinha()
