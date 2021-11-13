"""
Fazer um programa que solicite para ser inserido qualquer coisa e retornará para o 
usuário se é verdadeiro ou falso a condição definida. 
Use os métodos:
    - isnumeric
    - isalpha
    - isupper
    - isspace
"""

texto = input("Informe qualquer coisa: ")

# métodos string
# site: https://www.programiz.com/python-programming/methods/string/isnumeric

## método .isnumeric() verifica se a string é numerica
print("o texto é númerico ? ", texto.isnumeric())

print()
print(20 * "-=-")
## método .isalpha retorna True se todos os caracteres na string forem do alfabeto
print("É alpha ?: ", texto.isalpha())

print()
print(20 * "-=-")
## método .isupper() retorna True se todos as letras da string estão maiuscula
print()

print("O texto está maiusculo: ", texto.isupper())

print()
print(20 * "-=-")
## método isspace() retorna True se houver espaço na string
print()

print("tem espaço: ", texto.isspace())

print()
print(20 * "-=-")
## método .capitalize() converte o primeiro caracter em maiusculo
print("texto.capitalize() = ", texto.capitalize())


print()
print(20 * "-=-")
## método .center() retorna uma string que é preenchida com o caracter especificado
print("texto centralizado: ", texto.center(30, "="))


print()
print(20 * "-=-")
## método .count() retorna o número de ocorrencia de uma substring 
print(f"Número de ocorrência de 'a' em '{texto}' é ?", texto.count("a"))

print()
print(20 * "-=-")
## o método .isprintable()
print()

texto = """
Os métodos isprintable () retornam True se todos os 
caracteres na string forem imprimíveis ou
se a string estiver vazia. Caso contrário, retorna False.
"""
print(texto)
print(texto.isprintable())
