import json
import random
import re
import time
import requests

URL_BUSCA = "https://openlibrary.org/search.json"

AUTORES_BRASILEIROS = [
    ("Clarice Lispector", "Romance"),
    ("Machado de Assis", "Romance"),
    ("Conceição Evaristo", "Drama"),
    ("Cecília Meireles", "Poesia"),
    ("Lygia Fagundes Telles", "Contos"),
    ("Rachel de Queiroz", "Romance"),
    ("Carlos Drummond de Andrade", "Poesia"),
    ("Jorge Amado", "Romance"),
    ("José de Alencar", "Romance"),
    ("Graciliano Ramos", "Drama"),
    ("Aluísio Azevedo", "Romance"),
    ("Monteiro Lobato", "Fantasia"),
    ("Manuel Bandeira", "Poesia"),
    ("Lima Barreto", "Drama"),
    ("Érico Veríssimo", "Romance"),
]


def gerar_preco() -> float:
    return round(random.uniform(20, 100), 2)


def extrair_autor(item: dict, autor_padrao: str) -> str:
    autores = item.get("author_name", [])
    if autores:
        return autores[0].strip()
    return autor_padrao


def extrair_isbn(item: dict, contador_sem_isbn: int) -> str:
    isbns = item.get("isbn", [])
    if isbns:
        return str(isbns[0]).strip()
    return f"SEMISBN{contador_sem_isbn:05d}"


def titulo_portugues(titulo: str) -> bool:
    titulo_limpo = titulo.strip()

    if not titulo_limpo:
        return False

    # rejeita alfabetos não latinos
    if re.search(r"[А-Яа-яЁёΩωΑ-ω]", titulo_limpo):
        return False

    # rejeita títulos estrangeiros
    palavras_bloqueadas = {
        "the", "and", "of", "in", "on", "is", "none",
        "les", "il", "und", "sein", "zeit"
    }

    palavras = re.findall(r"[a-zA-ZÀ-ÿ']+", titulo_limpo.casefold())
    if palavras and palavras[0] in palavras_bloqueadas:
        return False

    return True


def normalizar_genero(genero_padrao: str) -> str:
    mapa = {
        "Romance": "Romance",
        "Drama": "Drama",
        "Poesia": "Poesia",
        "Contos": "Contos",
        "Fantasia": "Fantasia",
    }
    return mapa.get(genero_padrao, "Literatura")


def buscar_por_autor(autor: str, pagina: int = 1, limite: int = 100) -> list[dict]:
    params = {
        "author": autor,
        "language": "por",
        "page": pagina,
        "limit": limite,
    }

    headers = {
        "User-Agent": "CatalogoLivrosBusca/1.0"
    }

    resposta = requests.get(URL_BUSCA, params=params, headers=headers, timeout=30)
    resposta.raise_for_status()
    dados = resposta.json()
    return dados.get("docs", [])


def gerar_base_200_livros_portugues() -> list[dict]:
    livros = []
    isbns_usados = set()
    chaves_usadas = set()
    contador_sem_isbn = 1

    alvo_total = 200

    for autor_consulta, genero_padrao in AUTORES_BRASILEIROS:
        pagina = 1

        while len(livros) < alvo_total:
            resultados = buscar_por_autor(autor_consulta, pagina=pagina, limite=100)

            if not resultados:
                break

            adicionou_na_pagina = False

            for item in resultados:
                titulo = item.get("title", "").strip()
                if not titulo:
                    continue

                if not titulo_portugues(titulo):
                    continue

                autor = extrair_autor(item, autor_consulta)
                isbn = extrair_isbn(item, contador_sem_isbn)
                genero = normalizar_genero(genero_padrao)

                chave_unica = (
                    titulo.casefold(),
                    autor.casefold(),
                    isbn.casefold(),
                )

                if isbn in isbns_usados or chave_unica in chaves_usadas:
                    contador_sem_isbn += 1
                    continue

                livros.append({
                    "titulo": titulo,
                    "autor": autor,
                    "isbn": isbn,
                    "genero": genero,
                    "preco": gerar_preco()
                })

                isbns_usados.add(isbn)
                chaves_usadas.add(chave_unica)
                contador_sem_isbn += 1
                adicionou_na_pagina = True

                if len(livros) >= alvo_total:
                    break

            if not adicionou_na_pagina:
                break

            pagina += 1
            time.sleep(0.2)

        if len(livros) >= alvo_total:
            break

    return livros[:alvo_total]


def salvar_json(livros: list[dict], caminho: str = "livros.json") -> None:
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)


def main() -> None:
    livros = gerar_base_200_livros_portugues()
    salvar_json(livros)

    print(f"Base gerada com {len(livros)} livros em português.")
    print("Arquivo salvo em: livros.json")


if __name__ == "__main__":
    main()