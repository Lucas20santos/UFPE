from os import system
system("clear")

print("""
Informe:
1 - Sim
0 - Nao
""")
soma = 0

while True:
    try:
        resposta = int(input("Resposta: "))
    except:
        print("Informe uma resposta valida!")
    else:
        break
soma = soma + resposta

# outro pergunta....

