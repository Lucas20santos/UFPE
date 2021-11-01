from os import system as linux

pratos = []

while True:
    linux("clear")
    if len(pratos) == 0:
        print("Insira algum elemento na pilha de pratos.")
        pratos.append(int(input("Informe um elemento numerico: ")))
        for k,v in enumerate(pratos):
            print(f"Elemento {v} na posição {k}")
    else:
        opcao = input("Voce deseja inserir algum elemento: ")
        if opcao in "Ss":
            pratos.append(int(input("Informe um elemento numerico: ")))
            for k,v in enumerate(pratos):
                print(f"Elemento {v} na posição {k}")
    
        if len(pratos) >= 1:
            opcao = input("Voce deseja remover algum elemento ou digite qualquer tecla para continuar: ")
            if opcao in "Ss":
                pratos.pop()
            
            for k,v in enumerate(pratos):
                print(f"Elemento {v} na posição {k}")

    sair = input("Deseja continuar inserindo ou removendo ? Digite S[sim] outra letra sai do programa.").strip()[0].upper()
    if sair != "S":
        break
