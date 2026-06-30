from itens import Item


def mochila_dinamica(itens: list[Item], capacidade: int):

    n = len(itens)

    # dp[i][w] = melhor score utilizando os i primeiros itens
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preenchimento Bottom-Up
    for i in range(1, n + 1):

        item = itens[i - 1]

        score = item.valor * item.raridade

        for peso in range(capacidade + 1):

            if item.peso > peso:

                dp[i][peso] = dp[i - 1][peso]

            else:

                dp[i][peso] = max(
                    dp[i - 1][peso],
                    score + dp[i - 1][peso - item.peso]
                )

    
    # Backtracking (OPT)
  

    mochila = []

    peso = capacidade

    for i in range(n, 0, -1):

        if dp[i][peso] != dp[i - 1][peso]:

            item = itens[i - 1]

            mochila.append(item)

            peso -= item.peso

    mochila.reverse()

    peso_total = sum(item.peso for item in mochila)
    valor_total = sum(item.valor for item in mochila)
    score_total = sum(item.valor * item.raridade for item in mochila)

    return mochila, peso_total, valor_total, score_total, dp
    

def imprimir_tabela(dp, capacidade):
    print("\n========== TABELA DA PROGRAMAÇÃO DINÂMICA ==========\n")

    # Cabeçalho
    print("Item\\Peso", end="\t")
    for peso in range(capacidade + 1):
        print(f"{peso:>4}", end="")
    print()

    # Linhas da tabela
    for i, linha in enumerate(dp):
        print(f"{i:>4}", end="\t")
        for valor in linha:
            print(f"{valor:>4}", end="")
        print()