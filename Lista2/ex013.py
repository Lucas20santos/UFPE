"""
Mostre como converter:
a. Chaves do dicionário em uma lista
b. Valores do dicionário em uma lista
c. Dicionário em uma lista de tuplas, cujos elementos são as chaves e os valores
"""

# Letra a
dicionario = {"1": 1, "3": 2, "9": 4}

chaves = list(dicionario)
print("chaves = ",chaves)

# Letra B
valores = list(dicionario.values())
print("valores: ", valores)


# Letra c
listaDeTupla = []


for k, v in enumerate(dicionario):
    listaDeTupla.append((k, v))

print("Lista de Tupla: ", listaDeTupla)
