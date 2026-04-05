from __future__ import annotations
from livro import Livro

# nó de uma árvore binária de busca 
class No:
	def __init__(self, livro: Livro):
		self.livro = livro
		# a chave da ordenação é o título limpo do livro
		self.chave = livro.chave_busca()
		# filho à esquerda menores
		self.esquerda: No | None = None
		# filho a direita maiores (alfabeticamente)
		self.direita: No | None = None

	def __repr__(self) -> str:
		return f"No({self.livro!r})"