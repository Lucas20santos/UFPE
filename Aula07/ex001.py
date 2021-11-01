from os import system as linux
import numpy
linux("clear")

notas = []
print("Infore as notas do aluno: ")
cont = 0
soma = 0

for i in range(3):
    notas.append(float(input(f"Nota{i  + 1}: ")))

while cont < len(notas):
    print(f"Index {cont + 1} : nota {notas[cont]}")
    cont += 1

print(f"Media = {sum(notas)/ 3}")
