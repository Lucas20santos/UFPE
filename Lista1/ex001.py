from os import system
from sys import platform as SO

if SO == "linux" or SO == "linux2":
    system("clear")
elif SO == "win32":
    system("cls")

dias = int(input("Informe a quantidade de dia:: "))
horas = int(input("Informe a quantidade de horas:: "))
minutos = int(input("Informe a quantidade de minutos:: "))
segundos = int(input("Informe a quantidade de segundos:: "))

print("""
1 dia    = 86.400 segundos
1 hora   = 3.600  segundos
1 minuto = 60     segundos
""")

totalSegundos = dias * 86400 + horas * 3600 + minutos * 60 + segundos 

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} seguntos tem {totalSegundos} segundos.")
