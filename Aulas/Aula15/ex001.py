arq1 = open("par.txt", "w")
arq2 = open("Impar.txt", "w")

for x in range(1000):
    if x % 2 == 0:
        arq1.write(str(x) +"\n")
    else:
        arq2.write(str(x) +"\n")

arq1.close()
arq2.close()
