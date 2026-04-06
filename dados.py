# Dados do repositório

# Dados Aleatórios (para testes de desempenho)

import random
from faker import Faker
from livro import Livro

fake = Faker("pt_BR")


def gerar_livros_repositorio():
    return [
        Livro("A Hora da Estrela", "Clarice Lispector", "CL001", "Romance", 34.90),
        Livro("Perto do Coração Selvagem", "Clarice Lispector", "CL002", "Romance", 39.90),
        Livro("Laços de Família", "Clarice Lispector", "CL003", "Contos", 29.90),
        Livro("A Paixão Segundo G.H.", "Clarice Lispector", "CL004", "Romance", 42.90),
        Livro("O Lustre", "Clarice Lispector", "CL005", "Romance", 36.90),
        Livro("A Cidade Sitiada", "Clarice Lispector", "CL006", "Romance", 35.90),
        Livro("Um Sopro de Vida", "Clarice Lispector", "CL007", "Romance", 33.90),
        Livro("Água Viva", "Clarice Lispector", "CL008", "Ficção", 31.90),
        Livro("Felicidade Clandestina", "Clarice Lispector", "CL009", "Contos", 28.90),
        Livro("A Maçã no Escuro", "Clarice Lispector", "CL010", "Romance", 41.90),
        Livro("Uma Aprendizagem", "Clarice Lispector", "CL011", "Romance", 37.90),
        Livro("Alguns Contos", "Clarice Lispector", "CL012", "Contos", 26.90),
        Livro("A Bela e a Fera", "Clarice Lispector", "CL013", "Contos", 27.90),
        Livro("A Legião Estrangeira", "Clarice Lispector", "CL014", "Contos", 30.90),
    ]


def gerar_livros_aleatorios(qtd, isbn_inicial=1000):
    generos = [
        "Romance", "Fantasia", "Terror", "Suspense",
        "Drama", "Ficção Científica", "Distopia", "Contos"
    ]

    livros = []

    for i in range(qtd):
        titulo = fake.sentence(nb_words=3).replace(".", "")

        autor = fake.name()

        isbn = f"AL{isbn_inicial + i}"

        genero = random.choice(generos)

        preco = round(random.uniform(20, 100), 2)

        livros.append(Livro(titulo, autor, isbn, genero, preco))

    return livros


def gerar_base_mista(qtd_aleatorios=50, embaralhar=True):
    livros = gerar_livros_repositorio() + gerar_livros_aleatorios(qtd_aleatorios)

    if embaralhar:
        random.shuffle(livros)

    return livros