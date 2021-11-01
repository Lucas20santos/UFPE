print("====== Registro do Aluno ======")

nomeAluno = input("Informe o nome do aluno: ")
cpfAluno = input("Informe o CPF do Aluno: ")
periodoAluno = int(input("Informe o perído do Aluno: "))
pesoAluno = float(input("Informe o peso do aluno: "))

print("Nome Aluno {0:^26} {1}".format("-"* 26, nomeAluno))
print("CPF Aluno {0:^27} {1}".format("-" * 27, cpfAluno))
print("Periodo do Aluno {0:^20} {1}".format("-" *  20, periodoAluno))
print("Peso do Aluno {0:^23} {1}".format("-" * 23, pesoAluno))
