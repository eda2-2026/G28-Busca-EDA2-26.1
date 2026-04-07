from __future__ import annotations
import unicodedata


def normalizar_texto(texto: str) -> str:
    if texto is None:
        return ""
    texto_normalizado = unicodedata.normalize("NFKD", str(texto))
    texto_sem_acentos = "".join(
        caractere for caractere in texto_normalizado
        if not unicodedata.combining(caractere)
    )
    return texto_sem_acentos.casefold().strip()


class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str, genero: str, preco: float):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.preco = preco

    def chave_busca(self) -> str:
        return normalizar_texto(self.titulo)

    def exibir_info(self) -> str:
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"ISBN: {self.isbn}\n"
            f"Gênero: {self.genero}\n"
            f"Preço: R$ {self.preco:.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"Livro(titulo={self.titulo!r}, autor={self.autor!r}, "
            f"isbn={self.isbn!r}, genero={self.genero!r}, preco={self.preco!r})"
        )

    # função para ordenar LESS THAN - ordena de acordo com título limpo
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Livro):
            return NotImplemented
        return (self.chave_busca(), self.isbn) < (other.chave_busca(), other.isbn)

    # função para definir livros IGUAIS - somente se o isbn for igual
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Livro):
            return NotImplemented
        return self.isbn == other.isbn