from __future__ import annotations
from typing import Iterable
from livro import Livro, normalizar_texto


def buscar_livro_sequencial(livros: Iterable[Livro], termo: str | Livro) -> tuple[Livro | None, int]:
	# percorre lista de livros um a um
	# retorna o livro ou None
	# retorna o numero de tentativas
	chave_busca = _obter_chave_busca(termo)
	comparacoes = 0

	# busca sequencial
	for livro in livros:
		comparacoes += 1
		if livro.chave_busca() == chave_busca:
			return livro, comparacoes

	return None, comparacoes


def buscar_por_titulo(livros: Iterable[Livro], titulo: str) -> Livro | None:
	# função simplificada que retorna só o livro
	livro, _ = buscar_livro_sequencial(livros, titulo)
	return livro


def _obter_chave_busca(termo: str | Livro) -> str:
	if isinstance(termo, Livro):
		return termo.chave_busca()
	return normalizar_texto(termo)
