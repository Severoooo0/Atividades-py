num = int(input("Digite um número: "))

divisor = []

for i in range(2, num):
    if num % i == 0:
        divisor.append(i)

if num < 2:
    print("Não é primo")
elif len(divisor) == 0:
    print("É primo")
else:
    print("Não é primo")
    print("É divisível por:", divisor)
