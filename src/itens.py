from dataclasses import dataclass


RARIDADES = {
    1: "Comum⭐",
    2: "Incomum⭐⭐",
    3: "Raro⭐⭐⭐",
    4: "Epico⭐⭐⭐⭐",
    5: "Lendario⭐⭐⭐⭐⭐"
}


@dataclass
class Item:
    nome: str
    peso: int
    valor: int
    largura: int
    altura: int
    raridade: int
    tipo: str


ITENS = [

    # Consumíveis
    Item("Poção de Vida", 1, 10, 1, 1, 1, "Consumivel"),
    Item("Poção de Mana", 1, 12, 5, 5, 1, "Consumivel"),
    Item("Elixir Arcano", 2, 30, 1, 2, 3, "Consumivel"),

    # Armas
    Item("Adaga", 2, 15, 1, 2, 1, "Adaga"),
    Item("Espada Longa", 5, 40, 1, 3, 2, "Espada"),
    Item("Machado de Guerra", 8, 65, 2, 3, 3, "Machado"),
    Item("Arco Élfico BADASS", 4, 55, 2, 2, 4, "Arco"),
    Item("Cajado Arcano Muito Mágico", 6, 90, 1, 4, 5, "Magico"),

    # Armaduras
    Item("Escudo de Ferro", 6, 45, 2, 2, 2, "Armadura"),
    Item("Armadura Pesada", 10, 85, 2, 3, 4, "Armadura"),
    Item("Manto do Arquimago", 3, 100, 2, 2, 5, "Armadura"),

    # Tesouros
    Item("Anel de Ouro", 1, 50, 1, 1, 3, "Tesouro"),
    Item("Rubi Encantado", 2, 80, 1, 1, 4, "Tesouro"),
    Item("Relíquia Ancestral", 5, 140, 2, 2, 5, "Outro"),
]