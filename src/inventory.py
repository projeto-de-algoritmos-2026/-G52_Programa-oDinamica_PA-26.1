inventario = [
    ["⬛" for _ in range(8)]
    for _ in range(6)
]

EMOJIS = {
    "Espada": "⚔️",
    "Adaga": "🗡️",
    "Arco": "🏹",
    "Machado": "🪓",
    "Armadura": "🛡️",
    "Consumivel": "🧪",
    "Tesouro": "💎",
    "Magico": "🔮",
    "Outro": "📜",
}

def exibir_inventario(inventario: list[list[str]]):
    print("Inventário:")
    for linha in inventario:
        print(" ".join(linha))

def pode_posicionar(
    inventario,
    item,
    linha,
    coluna
):
    
    # Verifica limites do grid
    if linha + item.altura > len(inventario):
        return False

    if coluna + item.largura > len(inventario[0]):
        return False

    # Já está ocupado???
    for i in range(item.altura):
        for j in range(item.largura):

            if inventario[linha + i][coluna + j] != "⬛":
                return False

    return True

def posicionar_item(
    inventario,
    item,
    linha,
    coluna
):

    emoji = EMOJIS.get(item.tipo, "📦")

    for i in range(item.altura):
        for j in range(item.largura):

            inventario[linha + i][coluna + j] = emoji

def inserir_item(inventario, item):

    for linha in range(len(inventario)):

        for coluna in range(len(inventario[0])):

            if pode_posicionar(
                inventario,
                item,
                linha,
                coluna
            ):

                posicionar_item(
                    inventario,
                    item,
                    linha,
                    coluna
                )

                return True

    return False

def limpar_inventario(inventario):

    for i in range(len(inventario)):
        for j in range(len(inventario[0])):

            inventario[i][j] = "⬛"

      