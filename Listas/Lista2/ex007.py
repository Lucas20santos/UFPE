"""
Faça um programa que solicite a idade, nome, peso e altura dos alunos de uma academia
e armazene em uma variável composta. Cada elemento da variável composta deverá
representar as características de cada aluno.
a. O programa deve permitir que o usuário pesquise o nome do aluno e como
retorno o programa deverá fornecer se o aluno está obeso ou não (faça uma
calculadora de Índice de Massa Corporal- IMC).
b. Exiba uma lista ordenada com os nomes dos alunos cadastrados. (Deixe 5 alunos
cadastrados).
c. Exiba o nome e o IMC do aluno mais pesado e do aluno mais leve.
"""
from packages.organizar import criarLinha, limpar
from operator import itemgetter
limpar()

def embelezamento():
    criarLinha(num=70)
    criarLinha(70, " ", "Academia Boa Forma")
    criarLinha(num=70)
    criarLinha(num=70, completa=" ", texto=" CADASTRAMENTO ")
    criarLinha(num=70, completa="-",)

def inserirAluno(alunos):
    nome = input("Nome do Aluno: ").lower()
    idade = int(input("Idade do Aluno: "))
    peso = float(input("Peso do Aluno: "))
    altura = float(input("Altura do Aluno: "))

    alunos["nome"].append(nome)
    alunos["idade"].append(idade)
    alunos["peso"].append(peso)
    alunos["altura"].append(altura)
    imc = peso / (altura **2)
    alunos["IMC"].append(round(imc, 3))
    if imc < 18.5:
        alunos["Situacao"].append("Abaixo do Peso")
    elif imc >= 18.5 and imc < 24.9:
        alunos["Situacao"].append("Peso Normal")
    elif imc >= 24.9 and imc < 29.9:
        alunos["Situacao"].append("Sobrepeso")
    else:
        alunos["Situacao"].append("Obesidade")
    criarLinha(num=70, completa="-")

def pesquisarAlunos(alunos):
    if len(alunos) == 0:
        print("A lista ainda vázia!")
    else:
        nome = input("Informe o nome: ").lower()
        for k, v in enumerate(alunos["nome"]):
            if nome == v:
                print(f"""
                - Nome: {alunos['nome'][k]}
                - Idade: {alunos['idade'][k]}
                - Peso: {alunos['peso'][k]}
                - Altura: {alunos['altura'][k]}
                - IMC: {alunos['IMC'][k]}
                - Situação: {alunos['Situacao'][k]}""")
            else:
                print("Esse aluno não está cadastrado")

def alunoMaisPesado(alunos):
    for k, v in enumerate(alunos["peso"]):
        if v >= 100:
            print(f"Nome: {alunos['nome'][k]} - IMC: {alunos['IMC'][k]} - Situação: {alunos['Situacao'][k]}") 

def alunoMaisLeve(alunos):
    for k, v in enumerate(alunos["peso"]):
        if v <= 60:
            print(f"Nome: {alunos['nome'][k]} - IMC: {alunos['IMC'][k]} - Situação: {alunos['Situacao'][k]}")

def ordenarAlunos(alunos):
    print("Lista de Alunos: ")
    alunos["nome"].sort()
    for k, v in enumerate(alunos['nome']):
        print(f"{k + 1} - {v}")


########################################################## Código Principal ##################################################

Aluno = {
        "nome": [],
        "idade": [],
        "peso": [],
        "altura": [],
        "IMC": [], 
        "Situacao": []
    }
embelezamento()
# Aluno
while True:
    print("""
    1 - Inserir Novo Aluno
    2 - Pesquisar ALuno
    3 - Listar Alunos mais Pesados
    4 - Listar Alunos mais Leve
    5 - Ordenar Alunos
    6 - Sair
    """)
    criarLinha(25, "-")

    while True:
        try:
            opcao = int(input("Informe sua opcão: "))
        except:
            print("Opcão invalidada! DIgite um número entre 1 e 6")
        else:
            break
    
    if opcao == 1:
        inserirAluno(alunos=Aluno)
    elif opcao == 2:
        pesquisarAlunos(alunos=Aluno)
    elif opcao == 3:
        alunoMaisPesado(alunos=Aluno)
    elif opcao == 4:
        alunoMaisLeve(alunos=Aluno)
    elif opcao == 5:
        ordenarAlunos(alunos=Aluno)
    elif opcao == 6:
        break
    else: 
        print("Opcao for do intervalo. Digite novamente! ")
    input("Aperte Enter para continuar! ")
    limpar()
    embelezamento()

print("FIM")
