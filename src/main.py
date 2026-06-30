from itens import ITENS
from inventory import (
    inventario,
    limpar_inventario,
    inserir_item,
    exibir_inventario
)

from knapsack import knapsack as knapsackGuloso
from knapsackDinamico import (
    mochila_dinamica,
    imprimir_tabela
)

import time

CAPACIDADE = 20

while True:

    print("\n==============================")
    print(" INVENTÁRIO RPG ")
    print("==============================")
    print("1 - Algoritmo Guloso")
    print("2 - Programação Dinâmica")
    print("3 - Benchmark (Guloso x Dinâmica)")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        break

    limpar_inventario(inventario)

    # GULOSO

    if opcao == "1":

        mochila, peso_total, valor_total = knapsackGuloso(
            ITENS,
            CAPACIDADE,
            inventario,
            inserir_item
        )

    # DINÂMICA

    elif opcao == "2":

        mochila, peso_total, valor_total, score_total, dp = mochila_dinamica(
            ITENS,
            CAPACIDADE
        )

        print("\nReconstruindo solução ótima...\n")

        for item in mochila:

            print(f"🎒 {item.nome}")

            if inserir_item(inventario, item):
                print("   ✅ Inserido no inventário")
            else:
                print("   ❌ Não coube no inventário")

        imprimir_tabela(dp, CAPACIDADE)

    elif opcao == "3":

        print("\n========== BENCHMARK ==========\n")
    
    # GULOSO   

        limpar_inventario(inventario)

        inicio = time.perf_counter()

        mochila_g, peso_g, valor_g = knapsackGuloso(
            ITENS,
            CAPACIDADE,
            inventario,
            inserir_item
        )

        tempo_g = time.perf_counter() - inicio

        score_g = sum(
            item.valor * item.raridade
            for item in mochila_g
        )
  
    # DINÂMICA  

        limpar_inventario(inventario)

        inicio = time.perf_counter()

        mochila_d, peso_d, valor_d, score_d, dp = mochila_dinamica(
            ITENS,
            CAPACIDADE
        )

        tempo_d = time.perf_counter() - inicio

        print("=" * 70)
        print(f"{'Métrica':<20}{'Guloso':<20}{'Dinâmica'}")
        print("=" * 70)
        print(f"{'Tempo':<20}{tempo_g:.8f}s{'':<8}{tempo_d:.8f}s")
        print(f"{'Peso':<20}{peso_g:<20}{peso_d}")
        print(f"{'Valor':<20}{valor_g:<20}{valor_d}")
        print(f"{'Score':<20}{score_g:<20}{score_d}")
        print(f"{'Itens':<20}{len(mochila_g):<20}{len(mochila_d)}")

        print("\nItens escolhidos pelo Guloso:")
        for item in mochila_g:
            print(f"✔ {item.nome}")

        print("\nItens escolhidos pela Programação Dinâmica:")
        for item in mochila_d:
            print(f"✔ {item.nome}")

        input("\nPressione ENTER para voltar ao menu...")

        continue

    else:
        print("Opção inválida!")
        continue

    print("\n========== INVENTÁRIO ==========\n")

    exibir_inventario(inventario)

    print("\n========== ITENS ESCOLHIDOS ==========\n")

    for item in mochila:
        print(f"✔ {item.nome}")

    print("\n========== ESTATÍSTICAS ==========\n")

    print(f"Peso total : {peso_total}/{CAPACIDADE}")
    print(f"Valor total: {valor_total}")

    if opcao == "2":
        print(f"Score total: {score_total}")