from os import system as linux
linux("clear")

cadastro = {
    "alunos":[],
    "imc": []
    }
a = 0

if True:
    a = 10
    print(a)

for i in range(len(cadastro["alunos"])):
    a = 10
    if cadastro["imc"][i] > 30:
        a = 20
        print(f"IMC - Gordo")
    elif 25 < cadastro["imc"][i] <= 30:        
        print("IMC - Sobrepeso")
    else:
        print("IMC - Normal")

print(a)
