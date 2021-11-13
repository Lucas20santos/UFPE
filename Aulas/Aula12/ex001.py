from os import system as linux
linux("clear")

conjuntoA = {3, 4, 5, 6, 7, 41, 50, 83}
conjuntoB = {3, 4, 6, 8, 48, 78, 100}
conjuntoC = {1, 2, 6, 8, 60, 100}
conjuntoD = {4, 6, 7, 8, 21, 54, 60, 83}

# Letra A
print("================ Letra A ==================")
print(f"Conjunto A = {conjuntoA}")
print(f"Conjunto B = {conjuntoB}")
print(f"Conjunto C = {conjuntoD}")

# Letra B
print("================ Letra B ==================")
conjuntoInterQuatroConjuntos = conjuntoA & conjuntoB & conjuntoC & conjuntoD
print("Intersecção dos quatros Conjuntos:\n", conjuntoInterQuatroConjuntos)

# Letra C
print("================ Letra C ==================")
conjuntoUniaoQuatroConjuntos = conjuntoA | conjuntoB | conjuntoC | conjuntoD
print("Uniao dos Quatros conjuntos:\n",conjuntoUniaoQuatroConjuntos)

# Letra D
print("================ Letra D ==================")
uniaoAUD = (conjuntoA | conjuntoB)
print(uniaoAUD)
# Uniao A e B = {3, 4, 5, 6, 7, 8, 41, 48, 50, 54, 78,83,100}
diferencaUniaoAUD_ConjuntoD = uniaoAUD - conjuntoD
print(diferencaUniaoAUD_ConjuntoD)