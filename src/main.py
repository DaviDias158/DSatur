import sys
from graph import Graph
from dsatur import DSatur

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_do_arquivo>")
        return

    # Mapeamento de índices para nomes (UF)
    ufs = [
        "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", 
        "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", 
        "RO", "RR", "RS", "SC", "SE", "SP", "TO"
    ]

    try:
        with open(sys.argv[1], 'r') as f:
            v_count = int(f.readline())
            e_count = int(f.readline())
            g = Graph(v_count)
            for _ in range(e_count):
                v, w = map(int, f.readline().split())
                g.add_edge(v, w)
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return

    print("--- Lista de Adjacência ---")
    print(g)
    print("-" * 30)

    dsatur = DSatur(g)
    colors = dsatur.solve()

    print("\n--- Ordem de Coloração ---")
    order_names = [ufs[v] for v in dsatur.coloring_order]
    print(" -> ".join(order_names))

    print("\n--- Resultado da Coloração ---")
    for i in range(len(ufs)):
        print(f"{ufs[i]} (Índice {i}): Cor {colors[i]}")

    total_colors = len(set(colors))
    valid = dsatur.is_valid()

    print("\n" + "="*30)
    print(f"Total de cores utilizadas: {total_colors}")
    print(f"A coloração é válida? {'SIM' if valid else 'NÃO'}")
    print("="*30)

if __name__ == "__main__":
    main()
    