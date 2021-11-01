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


salarioPorHora = float(input("Quanto você recebe por hora trabalhada:: "))
horasTrabalho = int(input("Quantas horas você trabalha no mês:: "))

salarioNoMes = round(salarioPorHora * horasTrabalho, 4)
inss = salarioNoMes * 0.08
sindicato = salarioNoMes * 0.05
impostoDeRenda = salarioNoMes * 0.11
salarioLiquido = salarioNoMes - inss - sindicato - impostoDeRenda

salarioNoMes = locale.currency(salarioNoMes, grouping=True)
inss = locale.currency(inss, grouping=True)
sindicato = locale.currency(sindicato, grouping=True)
impostoDeRenda = locale.currency(impostoDeRenda, grouping=True)
salarioLiquido = locale.currency(salarioLiquido, grouping=True)

print(f"Seu salário bruto é: {salarioNoMes}!")
print(f"Você pagou ao INSS 8% do seu salário bruto que vale {inss}!")
print(f"Você pagou 5% ao sindicato que vale a {sindicato}!")
print(f"Seu salario líquido é: {salarioLiquido}!")
print(f"Você pagou 11% de Imposto de renda que vale a {impostoDeRenda}!")
