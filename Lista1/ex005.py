from os import system
from sys import platform as SO
import locale


if SO == "linux" or SO == "linux2":
    system("clear")
    local = locale.getlocale()
    locale.setlocale(locale.LC_MONETARY, local)
elif SO == "win32":
    system("cls")
    local = locale.getlocale()
    locale.setlocale(locale.LC_MONETARY, local)
else:
    print("Erro!!!")


salarioAtual = float(input("Informe seu salário atual:: "))
porcetagemAumento = float(input("Informe a porcetagem de aumento salarial:: "))
aumento = salarioAtual * porcetagemAumento / 100
salarioNovo = aumento + salarioAtual

aumento = locale.currency(aumento, grouping=True)
salarioNovo = locale.currency(salarioNovo, grouping=True)

print(f"O aumento do salário em reais foi de:: {aumento}!")
print(f"O novo salário do funcionário é:: {salarioNovo}!")
