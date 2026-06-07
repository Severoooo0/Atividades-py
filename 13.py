soma = 0
quantidade = 0

maior = None
menor = None

while True:
    temp = float(input("Digite uma temperatura (999 para encerrar): "))

    if temp == 999:
        break

    soma += temp
    quantidade += 1

    if maior is None or temp > maior:
        maior = temp

    if menor is None or temp < menor:
        menor = temp

media = soma / quantidade

print("Menor temperatura:", menor)
print("Maior temperatura:", maior)
print("Média das temperaturas:", media)
