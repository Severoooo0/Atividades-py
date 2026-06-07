while True:
    print("\nLojas Tabajara")

    total = 0
    produto = 1

    while True:
        valor = float(input(f"Produto {produto}: R$ "))

        if valor == 0:
            break

        total += valor
        produto += 1

    print(f"Total: R$ {total:.2f}")

    dinheiro = float(input("Dinheiro: R$ "))
    troco = dinheiro - total

    print(f"Troco: R$ {troco:.2f}")
