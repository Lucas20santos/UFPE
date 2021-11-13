num = int(input("Informe um número: "))

cont = 0

while cont <= num:
    if(cont % 2 == 1):
        cont += 1
        continue
    print(cont)
    cont += 1
    

