from __future__ import annotations
from typing import Iterable
from livro import Livro, normalizar_texto
from no import No


class ArvoreBST:
	def __init__(self):
		# a raiz é o primeiro livro inserido
		self.raiz: No | None = None
		self._tamanho = 0

	def inserir(self, livro: Livro) -> None:
		if self.raiz is None:
			self.raiz = No(livro)
			self._tamanho = 1
			return

		# se já existe raiz, desce recursivo pelos nós
		self._inserir_recursivo(self.raiz, livro)
		self._tamanho += 1

	def _inserir_recursivo(self, no_atual: No, livro: Livro) -> None:
		# usa LESS THAN de livro para decidir lado que o livro irá
		if livro < no_atual.livro:
			if no_atual.esquerda is None:
				no_atual.esquerda = No(livro)
			else:
				self._inserir_recursivo(no_atual.esquerda, livro)
		else:
			if no_atual.direita is None:
				no_atual.direita = No(livro)
			else:
				self._inserir_recursivo(no_atual.direita, livro)

	def buscar(self, termo: str | Livro) -> Livro | None:
		livro, _ = self.buscar_com_comparacoes(termo)
		return livro

	def buscar_com_comparacoes(self, termo: str | Livro) -> tuple[Livro | None, int]:
		chave_busca = self._obter_chave_busca(termo)
		comparacoes = 0
		no_atual = self.raiz

		# percorre árvore sem recursão
		while no_atual is not None:
			comparacoes += 1
			if chave_busca == no_atual.chave:
				return no_atual.livro, comparacoes
			if chave_busca < no_atual.chave:
				no_atual = no_atual.esquerda
			else:
				no_atual = no_atual.direita

		return None, comparacoes

	# percurso EM ORDEM - ordem alfabetica
	def em_ordem(self) -> list[Livro]:
		livros: list[Livro] = []
		self._em_ordem_recursivo(self.raiz, livros)
		return livros

	def _em_ordem_recursivo(self, no_atual: No | None, livros: list[Livro]) -> None:
		if no_atual is None:
			return
		self._em_ordem_recursivo(no_atual.esquerda, livros)
		livros.append(no_atual.livro)
		self._em_ordem_recursivo(no_atual.direita, livros)

	def construir(self, livros: Iterable[Livro]) -> None:
		for livro in livros:
			self.inserir(livro)

	@property
	# retorna quantidade de livros inseridos
	def tamanho(self) -> int:
		return self._tamanho

	@staticmethod
	# auxilia para converter string ou objeto em chave normalizada
	def _obter_chave_busca(termo: str | Livro) -> str:
		if isinstance(termo, Livro):
			return termo.chave_busca()
		return normalizar_texto(termo)

# função para criar árvore
def construir_arvore(livros: Iterable[Livro]) -> ArvoreBST:
	arvore = ArvoreBST()
	arvore.construir(livros)
	return arvore