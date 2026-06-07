soma_veiculos = 0
soma_acidentes_menos2000 = 0
qtd_cidades_menos2000 = 0

for i in range(5):
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos: "))
    acidentes = int(input("Número de acidentes: "))

    if i == 0:
        maior = menor = acidentes
        cidade_maior = cidade_menor = codigo

    if acidentes > maior:
        maior = acidentes
        cidade_maior = codigo

    if acidentes < menor:
        menor = acidentes
        cidade_menor = codigo

    soma_veiculos += veiculos

    if veiculos < 2000:
        soma_acidentes_menos2000 += acidentes
        qtd_cidades_menos2000 += 1

media_veiculos = soma_veiculos / 5

print("\nMaior índice de acidentes:", maior)
print("Cidade:", cidade_maior)

print("\nMenor índice de acidentes:", menor)
print("Cidade:", cidade_menor)

print("\nMédia de veículos:", media_veiculos)

if qtd_cidades_menos2000 > 0:
    media_acidentes = soma_acidentes_menos2000 / qtd_cidades_menos2000
    print("Média de acidentes nas cidades com menos de 2000 veículos:", media_acidentes)
else:
    print("Nenhuma cidade possui menos de 2000 veículos.")
