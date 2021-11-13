"""Crie um programa que exiba uma listagem de preços de produtos em forma tabular.
Utilize uma tupla única com nomes e preços dos produtos.
"""
produtoPreco = ("feijao", 10, "arroz", 20, "macarrao", 30, "picole", 40)

for i in range(0, len(produtoPreco), 2):
    print(str(produtoPreco[i]) +" " + "".center(40, ".") + " " +  str(produtoPreco[i + 1]))
