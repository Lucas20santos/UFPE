"""
Faça um programa insira em um dicionário vários nomes de pessoas e respectivas
idades. APENAS DEPOIS que tiver inserido todos os dados no dicionário, criar
uma lista com o nome das pessoas com idade acima de 30 anos e outra lista com o
nome das pessoas com idade abaixo de 30 anos.
"""
from packages.organizar import limpar
limpar()


pessoas = {
    "nome":[],
    "idade": []
}

while True:
    pessoas["nome"].append(input("Digite o nome da pessoa: ").lower().strip())
    while True:
        try:
            pessoas["idade"].append(int(input("Informe a idade da pessoa! ")))
        except:
            print("Informe um valor valido! ")
        else:
            break
    
    opcao = input("Deseja continuar? S - sim e N - Não ").strip()
    while opcao not in "SsNn":
        opcao = input("Erro!! Deseja continuar? S - sim e N - Não ").strip()

    if opcao in "Nn":
        break


abaixo30 = []
acima30  = []

for x in range(len(pessoas["nome"])):
    if pessoas["idade"][x] >= 30:
        acima30.append(pessoas["nome"][x])
    else:
        abaixo30.append(pessoas["nome"][x])

print(f"As pessoas que tem idade abaixo de 30 anos são: {abaixo30}")
print(f"As pessoas que tem idade acima ou igua a 30 anos são: {acima30}")
