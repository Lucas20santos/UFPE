from os import system as linux
linux("clear")
"""
Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo
segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para
calcular o resultado.
"""

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número:: "))
aux = 0
resto = 0
quociente = 0

while num1 >= num2:
    if num1 >= num2:
        num1 = num1 - num2
        quociente += 1

resto = num1
print(f"quociente = {quociente} <-> resto = {resto}")
