from os import system
from sys import platform as SO

if SO == "linux" or SO == "linux2":
    system("clear")
elif SO == "win32":
    system("cls")

print("Informe seu salário e veja se você deve ou não pagar imposto")


while True:
    opcao = input("Deseja verificar seu imposto:[s - sim e n - não]").strip()[0]

    while opcao not in "nNsS":
        opcao = input("Erro!!! Informe s/sim ou n/não: ")
  
    if opcao in "nN":
        break
  
    salario = float(input("Informe seu salário:: "))

    if salario > 1200:
        print("Você precisa pagar seu imposto!")
    else:
        print("Você não precisa pagar imposto!")
    
    print("Obrigado!")
    print("A receita federal agradece!")
    input("Aperte enter para continuar")

print("FIM")
