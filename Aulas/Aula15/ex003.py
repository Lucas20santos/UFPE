def arquivarFrase(texto, nomeArquivo):
    arq = open(nomeArquivo, "w")
    arq.write(texto)
    arq.close()


def lerImprimirArquivo(arquivo):
    arq = open(arquivo, "r")
    lista = arq.readlines()
    print("IMPRESSÃO DO TEXTO".center(50))
    for x in lista:
        print(x)


nomeArquivo = "FRASE.txt"
texto = input("Informe o texto ou frase: ")
arquivarFrase(texto=texto, nomeArquivo=nomeArquivo)
lerImprimirArquivo(arquivo=nomeArquivo)
