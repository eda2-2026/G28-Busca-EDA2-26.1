import json
import re


def titulo_valido(titulo: str) -> bool:
    titulo = titulo.strip()

    # remove títulos vazios
    if not titulo:
        return False

    # remove alfabetos não latinos (russo, grego, etc)
    if re.search(r"[А-Яа-яЁёΩωΑ-ω]", titulo):
        return False

    # remove títulos com muitos números ou símbolos estranhos
    if re.search(r"\[.*?\]", titulo):  # exemplo: [i.e.]
        return False

    # remove títulos que começam com número
    if re.match(r"^\d", titulo):
        return False

    # remove títulos que começam com palavras comuns em inglês (sugestão de títulos estrangeiros)
    palavras_ingles = {"the", "and", "of", "in", "on", "is", "none"}
    palavras = re.findall(r"[a-zA-ZÀ-ÿ']+", titulo.casefold())

    if palavras and palavras[0] in palavras_ingles:
        return False

    return True


def limpar_json(caminho_entrada="livros.json", caminho_saida="livros_limpos.json"):
    with open(caminho_entrada, "r", encoding="utf-8") as f:
        livros = json.load(f)

    livros_filtrados = []

    for livro in livros:
        titulo = livro.get("titulo", "")

        if titulo_valido(titulo):
            livros_filtrados.append(livro)

    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(livros_filtrados, f, ensure_ascii=False, indent=4)

    print(f"Antes: {len(livros)} livros")
    print(f"Depois: {len(livros_filtrados)} livros")
    print("Arquivo salvo como livros_limpos.json")


if __name__ == "__main__":
    limpar_json()