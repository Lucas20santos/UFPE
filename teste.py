arq = open("linha.txt", "w")

for x in range(0, 51):
    arq.write(str(x) + "\n")

arq.close()
