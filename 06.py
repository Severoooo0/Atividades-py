eleitor = int(input("Número total de eleitores: "))

cand1 = 0
cand2 = 0
cand3 = 0

for i in range(eleitor):
    voto = int(input(f"Eleitor {i+1}, vote (1, 2 ou 3): "))

    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    else:
        print("Voto inválido!")

print("\nResultado da eleição:")
print("Candidato 1:", cand1, "votos")
print("Candidato 2:", cand2, "votos")
print("Candidato 3:", cand3, "votos")
