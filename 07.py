turmas = int(input("Quantidade de turmas: "))

t_alunos = 0

for i in range(turmas):
    alunos = int(input(f"Quantidade de alunos da turma {i+1}: "))

    while alunos > 40:
        print("Uma turma não pode ter mais de 40 alunos.")
        alunos = int(input(f"Quantidade de alunos da turma {i+1}: "))

    t_alunos += alunos

media = t_alunos / turmas

print("Número médio de alunos por turma:", media)
