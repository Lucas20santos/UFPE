print("Usando o laço FOR: ")


print("1° Resolução com FOR")
for i in range(10, 4, -1):
	print(i)


print("2° Resolução com FOR")
cont = 10
for i in range(6):
	print(cont)
	if cont == 5:
		break
	else:
		cont -= 1

print("3° Resolução com FOR")

for i in range(6):
	print(f"{10 - i}")
