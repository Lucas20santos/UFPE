from os import system
from sys import platform as SO

if SO == "linux" or SO == "linux2":
    system("clear")
elif SO == "win32":
    system("cls")
else:
    print("Erro!!!")

leituraString1 = input("Informe uma primeira string:: ").strip().lower()
leituraString2 = input("Informe uma segundo string::: ").strip().lower()
tamanhoString1 = len(leituraString1)
tamanhoString2 = len(leituraString2)


print(50 * "=")
print("Informando o conteúdo: ")
print(f"O contéudo da primeira string é {leituraString1}")
print(f"O contéudo da segunda  string é {leituraString2}")

print(50 * "=")
print("Informando o tamanho das strings")
print(f"A primeira string, '{leituraString1}', tem um tamanho de {tamanhoString1} caracteres.")
print(f"A primeira string, '{leituraString2}', tem um tamanho de {len(leituraString2)} caracteres.")

print(50 * "=")
tamanhoString = "igual" if tamanhoString1 == tamanhoString2 else "diferente"
print(f"O tamanho das duas strings é {tamanhoString}")

print(50 * "=")
conteudoString = "igual" if leituraString1 == leituraString2 else "diferente"
print(f"O conteúdo das duas strings é {conteudoString}")
print(50 * "=")
