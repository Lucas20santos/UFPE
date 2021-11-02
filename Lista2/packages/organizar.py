from os import system as linux

def limpar():
    linux("clear")

def criarLinha(num=50, completa="=", texto=""):
    print(f"{texto}".center(num, completa))
