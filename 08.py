qtd_cds = int(input("Quantidade de CDs: "))

total = 0

for i in range(qtd_cds):
    valor = float(input(f"Valor do CD {i+1}: R$ "))
    total += valor

media = total / qtd_cds

print("Valor total investido: R$", total)
print("Valor médio por CD: R$", media)
