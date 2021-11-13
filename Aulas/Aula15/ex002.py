arq = open("par.txt", "r")
arq2 = open("multiplos4.txt", "w")

lista = arq.readlines()

for x in lista:
    if x != " ":
        num = int(x)
    else:
        arq2.write("---------------")
        continue

    if num % 4 == 0:
        arq2.write(str(num) + "\n")

arq2.close()
arq.close()
