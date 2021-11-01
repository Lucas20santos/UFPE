from os import system as linux
linux("clear")

num1 = int(input("Digite o primeiro número:: "))
num2 = int(input("Digite o segundo  número:: "))

quociente = 0
resto = 0

while num1 >= num2:
    if num1 >= num2:
        num1 -= num2
        quociente += 1

resto = num1
print(f"quociente = {quociente} - resto = {resto}")
