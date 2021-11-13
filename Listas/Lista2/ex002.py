"""Escreva um programa que faça 5 perguntas para uma pessoa sobre um crime. As
perguntas são:
• "Telefonou para a vítima?"
• "Esteve no local do crime?"
• "Mora perto da vítima?"
• "Devia para a vítima?"
• "Já trabalhou com a vítima?"
No final o programa deve imprimir uma classificação sobre a participação da pessoa
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
contrário, ele será classificado como "Inocente"."""
from os import system as linux
linux("clear")

def respostaPergunta(opcao):
    if opcao ==  "S":
        soma = 1
    else:
        soma = 0
    return soma

def analisePolicial(*args):
    soma = 0
    situacao = ""

    for i in args:
        opcao = input(i).upper().strip()[0]
        while opcao not in "SN":
            print("Por favor só informar SIM ou Não!")
        soma += respostaPergunta(opcao)
    
    if soma == 2:
        situacao = "Suspeito"
    elif soma == 3 or soma == 4:
        situacao = "Cumplice"
    elif soma == 5:
        situacao == "Assassino"
    else:
        situacao = "Inocente"
    
    return situacao

situacaoSuspeito = analisePolicial("Telefonou para a vítima?","Esteve no local do crime?"
,"Mora perto da vítima?" ,"Devia para a vítima?" ,"Já trabalhou com a vítima?")

print(f"O cidadao fulano é {situacaoSuspeito}")

# def myFunction(**kwargs):
#     for i in kwargs.items():
#         print(i)


# myFunction(name="Lucas", age=12)


# https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/
# https://medium.com/rafaeltardivo/python-entendendo-o-uso-de-args-e-kwargs-em-fun%C3%A7%C3%B5es-e-m%C3%A9todos-c8c2810e9dc8
# https://github.com/Lucas20santos/UFPE
