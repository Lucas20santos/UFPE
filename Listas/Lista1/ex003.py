from os import system
from sys import platform as SO

if SO == "linux" or SO == "linux2":
    system("clear")
elif SO == "win32":
    system("cls")

primeiroNumeroInteiro = int(input("Infome um número inteiro:: "))         
segundoNumeroInteiro = int(input("Informe um segundo numero inteiro:: ")) 
numeroReal = float(input("Informe um número real:: "))                    

print(20 * "= ")
print("Letra A")
print(f"(2 X {primeiroNumeroInteiro}) X ({segundoNumeroInteiro / 2}) = {(2 * primeiroNumeroInteiro) * (segundoNumeroInteiro / 2)}")

print(20 * "= ")
print("Letra B")
print(f"3 X {primeiroNumeroInteiro} + {numeroReal} = {3 * primeiroNumeroInteiro + numeroReal}")

print(20 * "= ")
print("Letra C")
print(f"{numeroReal}^3 = {numeroReal ** 3}")

print(20 * "= ")
