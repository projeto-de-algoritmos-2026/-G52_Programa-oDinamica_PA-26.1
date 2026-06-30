from itens import Item, RARIDADES


def knapsack(
    itens,
    capacidade,
    inventario,
    inserir_item
):

    itens_ordenados = sorted(
        itens,
        key=lambda item:
            (item.valor * item.raridade)
            / item.peso,
        reverse=True
    )

    mochila = []

    peso_total = 0
    valor_total = 0

    for item in itens_ordenados:

        score = (
            item.valor * item.raridade
        ) / item.peso

        print(f"\n🎯 Tentando pegar: {item.nome}")
        print(f"Score: {score:.2f}")
        print(f"Tamanho: {item.largura}x{item.altura}")
        print(f"Raridade: {RARIDADES[item.raridade]}")

        # Verifica peso
        if peso_total + item.peso > capacidade:

            print(
                f"❌ {item.nome} ultrapassa o limite de peso!"
            )

            continue

        # Tenta encaixar no grid
        sucesso = inserir_item(
            inventario,
            item
        )

        if sucesso:

            mochila.append(item)

            peso_total += item.peso
            valor_total += item.valor

            print(
                f"✅ {item.nome} inserido na mochila!"
            )

        else:

            print(
                f"❌ {item.nome} não coube no inventário!"
            )

    return mochila, peso_total, valor_total