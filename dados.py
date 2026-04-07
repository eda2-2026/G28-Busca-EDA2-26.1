import json
from livro import Livro


def carregar_livros_json(caminho_arquivo: str = "livros.json") -> list[Livro]:
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    livros = []
    for item in dados:
        livros.append(
            Livro(
                item["titulo"],
                item["autor"],
                item["isbn"],
                item["genero"],
                float(item["preco"])
            )
        )

    return livros