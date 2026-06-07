for i in range(10):
    numero = int(input("Número do aluno: "))
    altura = float(input("Altura (cm): "))

    if i == 0:
        num_alto = num_baixo = numero
        maior_altura = menor_altura = altura

    if altura > maior_altura:
        maior_altura = altura
        num_alto = numero

    if altura < menor_altura:
        menor_altura = altura
        num_baixo = numero

print("\nAluno mais alto:")
print("Número:", num_alto)
print("Altura:", maior_altura, "cm")

print("\nAluno mais baixo:")
print("Número:", num_baixo)
print("Altura:", menor_altura, "cm")
