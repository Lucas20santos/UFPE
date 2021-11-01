from os import system
from sys import platform as SO
from random import randint as ferias

if SO == "linux" or SO == "linux2":
    system("clear")
elif SO == "win32":
    system("cls")
else:
    print("Erro!!!")

diaDoMes = int(input("Informe o dia do Mes que você saiu de férias:: "))
diaSemana = input("Informe o dia da semana que você saiu de féiras:: ")
diasDeFerias = ferias(30, 120)

print(f"""Você terá umas férias maravilhosas que começam no dia {diaDoMes}, {diaSemana} e retornar
das suas férias depois de {diasDeFerias} noites.""")
