from __future__ import annotations
import unicodedata
import uuid

def normalizar_texto(texto: str) -> str:
	if texto is None:
		return ""
	texto_normalizado = unicodedata.normalize("NFKD", str(texto))
	texto_sem_acentos = "".join(
		caractere for caractere in texto_normalizado if not unicodedata.combining(caractere)
	)
	return texto_sem_acentos.casefold().strip()


class Livro:
	def __init__(self, titulo: str, autor: str, caminho_imagem: str, id: str | None = None):
		self.id = id or str(uuid.uuid4())
		self.titulo = titulo
		self.autor = autor
		self.caminho_imagem = caminho_imagem

	def to_dict(self) -> dict:
		return {
			"id": self.id,
			"titulo": self.titulo,
			"autor": self.autor,
			"caminho_imagem": self.caminho_imagem,
		}

	@staticmethod
	def from_dict(dados: dict) -> "Livro":
		return Livro(
			dados["titulo"],
			dados["autor"],
			dados["caminho_imagem"],
			dados.get("id"),
		)

	def chave_busca(self) -> str:
		return normalizar_texto(self.titulo)

	def exibir_info(self) -> str:
		return f"{self.titulo} - {self.autor}"

	def __repr__(self) -> str:
		return f"Livro(titulo={self.titulo!r}, autor={self.autor!r})"

	def __lt__(self, other: object) -> bool:
		if not isinstance(other, Livro):
			return NotImplemented
		return (self.chave_busca(), self.id) < (other.chave_busca(), other.id)

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Livro):
			return NotImplemented
		return self.id == other.id