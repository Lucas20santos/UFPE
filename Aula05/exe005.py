print("Resolução com laço While")

print("1° Resolução: ")
cont = 10
while True:
	print(cont)
	if cont == 5:
		break
	cont -= 1

print("2° Resolução: ")
cont = 10
while cont != 4:
	print(cont)
	cont -= 1

print("3° Resolução")
cont = 0
while 10 - cont != 4:
	print(10 - cont)
	cont += 1

