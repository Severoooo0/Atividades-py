n = int(input("Digite um número: "))
divisoes = 0

print("Números primos:")

for num in range(2, n + 1):
    primo = True

    for i in range(2, num):
        divisoes += 1
        if num % i == 0:
            primo = False
            break

    if primo:
        print(num)

print("Total de divisões:", divisoes)
