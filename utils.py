import time
from livro import Livro
from busca_sequencial import buscar_livro_sequencial
from arvore import ArvoreBST


def exibir_livro(livro: Livro | None) -> None:
    if livro is None:
        print("\nLivro não encontrado.\n")
        return

    print("\n=== Livro encontrado ===")
    print(livro.exibir_info())
    print()


def listar_livros(livros: list[Livro]) -> None:
    if not livros:
        print("\nNenhum livro cadastrado.\n")
        return

    print("\n=== Lista de Livros ===\n")
    for i, livro in enumerate(livros, start=1):
        print(f"Livro {i}")
        print(livro.exibir_info())
        print("-" * 30)
    print()


def medir_busca_sequencial(livros: list[Livro], termo: str) -> dict:
    inicio = time.perf_counter()
    livro, comparacoes = buscar_livro_sequencial(livros, termo)
    fim = time.perf_counter()

    return {
        "livro": livro,
        "comparacoes": comparacoes,
        "tempo": fim - inicio
    }


def medir_busca_bst(arvore: ArvoreBST, termo: str) -> dict:
    inicio = time.perf_counter()
    livro, comparacoes = arvore.buscar_com_comparacoes(termo)
    fim = time.perf_counter()

    return {
        "livro": livro,
        "comparacoes": comparacoes,
        "tempo": fim - inicio
    }


def comparar_buscas(livros: list[Livro], arvore: ArvoreBST, termo: str) -> None:
    resultado_seq = medir_busca_sequencial(livros, termo)
    resultado_bst = medir_busca_bst(arvore, termo)

    print("\n=== Comparação de Desempenho ===\n")

    print("Busca Sequencial:")
    print(f"Comparações: {resultado_seq['comparacoes']}")
    print(f"Tempo: {resultado_seq['tempo']:.8f} segundos\n")

    print("Árvore Binária de Busca:")
    print(f"Comparações: {resultado_bst['comparacoes']}")
    print(f"Tempo: {resultado_bst['tempo']:.8f} segundos\n")

    if resultado_bst["livro"] is not None:
        print("Livro encontrado:")
        print(resultado_bst["livro"].exibir_info())
    else:
        print("Livro não encontrado.")
    print()