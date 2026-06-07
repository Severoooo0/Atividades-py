soma_altura = 0
soma_peso = 0
quantidade = 0

while True:
    codigo = int(input("Código do cliente (0 para sair): "))

    if codigo == 0:
        break

    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    if quantidade == 0:
        cod_alto = cod_baixo = cod_gordo = cod_magro = codigo
        maior_altura = menor_altura = altura
        maior_peso = menor_peso = peso

    if altura > maior_altura:
        maior_altura = altura
        cod_alto = codigo

    if altura < menor_altura:
        menor_altura = altura
        cod_baixo = codigo

    if peso > maior_peso:
        maior_peso = peso
        cod_gordo = codigo

    if peso < menor_peso:
        menor_peso = peso
        cod_magro = codigo

    soma_altura += altura
    soma_peso += peso
    quantidade += 1

print("\nCliente mais alto:")
print("Código:", cod_alto, "- Altura:", maior_altura)

print("\nCliente mais baixo:")
print("Código:", cod_baixo, "- Altura:", menor_altura)

print("\nCliente mais gordo:")
print("Código:", cod_gordo, "- Peso:", maior_peso)

print("\nCliente mais magro:")
print("Código:", cod_magro, "- Peso:", menor_peso)

print("\nMédia das alturas:", soma_altura / quantidade)
print("Média dos pesos:", soma_peso / quantidade)
