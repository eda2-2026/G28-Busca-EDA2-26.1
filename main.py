from dados import carregar_livros_json
from arvore import construir_arvore
from utils import exibir_livro, listar_livros, comparar_buscas


def exibir_menu() -> None:
    print("=" * 50)
    print("        CATÁLOGO DE LIVROS - BUSCA")
    print("=" * 50)
    print("1. Listar livros em ordem alfabética")
    print("2. Buscar livro por título na BST")
    print("3. Comparar busca sequencial e BST")
    print("4. Mostrar quantidade de livros")
    print("0. Sair")
    print("=" * 50)


def main() -> None:
    try:
        livros = carregar_livros_json("livros_limpos.json")
    except FileNotFoundError:
        print("\nArquivo 'livros.json' não encontrado.")
        print("Execute primeiro: python3 gerar_base.py\n")
        return

    arvore = construir_arvore(livros)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            livros_ordenados = arvore.em_ordem()
            listar_livros(livros_ordenados)

        elif opcao == "2":
            titulo = input("\nDigite o título do livro: ").strip()
            livro = arvore.buscar(titulo)
            exibir_livro(livro)

        elif opcao == "3":
            titulo = input("\nDigite o título do livro para comparar as buscas: ").strip()
            comparar_buscas(livros, arvore, titulo)

        elif opcao == "4":
            print(f"\nQuantidade de livros cadastrados: {arvore.tamanho}\n")

        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()