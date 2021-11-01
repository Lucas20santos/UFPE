cont = 0
soma = 0

while True:
    num = float(input("informe números: "))
    cont += 1
    soma += num
    if num < 0 or num > 10:
        break

print(f"soma = {soma} quantidade = {cont}")
