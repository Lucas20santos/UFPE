"""Utilizando o while faça um programa que imprima a
pontuação obtida por determinado aluno em uma prova
de 3 questões, dado que cada questão vale 1 ponto.

Q1 - letra 'b'
Q2 - letra 'a'
Q3 - letra 'd'
"""
from os import system as linux
linux("clear")

print("+" + 20 * " =" + " +")
print("|" + "BOLETIM DO ALUNO".center(40) + " |")
print("+" + 20 * " =" + " +")
print()

alternativas = ['a', 'b', 'c', 'd', 'e']
respostasCertas = ['b', 'a', 'd']
resposAluno = []


soma = 0

for x in range(0, len(respostasCertas)):
    respostaQuestao = input(f"Resposta Questão {x}: ").lower()
    
    while respostaQuestao not in alternativas:
        respostaQuestao = input(f"Informe uma alternativa validade!!! Resposta Questão {x}").lower()

    resposAluno.append(respostaQuestao)
    if respostaQuestao == respostasCertas[x]:
        soma += 1

print()
print(20 * " =")
print(f"Resposta aluno: {resposAluno}".center(40))
print(f"PONTUAÇÃO DO ALUNO: {soma}".center(40))
print(20 * " =")
