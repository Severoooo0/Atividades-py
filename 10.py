preco = float(input("Preço do pão: R$ "))

print("\nPanificadora Pão de Ontem - Tabela de preços")

for i in range(1, 51):
    print(f"{i} - R$ {i * preco:.2f}")
