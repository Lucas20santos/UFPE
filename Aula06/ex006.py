from os import system as linux
linux("clear")
"""
Faça um código que solicite ao usuário que digite uma palavra e que rode até que a
palavra “sair” seja digitada.

- Um aviso deve ser exibido caso a palavra digitada seja =< 3 caracteres. O loop deve ser 
executado do início, solicitando uma nova palavra ao usuário.

- Um aviso seve se exibido, caso qualquer outra palavra, diferente de “sair” seja digitada.

- Caso a palavra seja “sair” deverá ser exibida uma mensagem e o loop deve ser finalizado.
"""

print("Digite uma palavra: ")

while True:
    palavra = input("-> ").lower().strip()
    
    if len(palavra) <= 3:
        print("Palavra até 3 caracteres!!!")
    elif palavra == "sair":
        break
    else:
        print("voce não digitou 'SAIR'")
