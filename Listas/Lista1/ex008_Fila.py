from os import system
from sys import platform as SO

if SO == "linux" or SO == "linux2":
    system("clear")
elif SO == "win32":
    system("cls")
else:
    print("Erro!!!")

banco = list()

while True:
    if len(banco) == 0:
        print("Insira algum elemento na pilha de pratos.")
        banco.append(int(input("Informe um elemento numerico: ")))
        for k,v in enumerate(banco):
            print(f"Elemento {v} na posição {k}")
    else:
        opcao = input("Voce deseja inserir algum elemento: ")
        if opcao in "Ss":
            banco.append(int(input("Informe um elemento numerico: ")))
            for k,v in enumerate(banco):
                print(f"Elemento {v} na posição {k}")
    
        if len(banco) >= 1:
            opcao = input("Voce deseja remover algum elemento ou digite qualquer tecla para continuar: ")
            if opcao in "Ss":
                banco.pop(0)
            
            for k,v in enumerate(banco):
                print(f"Elemento {v} na posição {k}")

    sair = input("Deseja continuar inserindo ou removendo ? Digite S[sim] outra letra sai do programa.").strip()[0].upper()
    if sair != "S":
        break
