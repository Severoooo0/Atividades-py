salario = float(input("Digite o salário inicial: R$ "))

aumento = 1.5 / 100

for ano in range(1996, 2027):
    salario += salario * aumento
    aumento *= 2

print(f"Salário atual: R$ {salario:.2f}")
