import json
from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: float | None

    with open('aula178.json', 'r') as arquivo:
        dados = json.load(arquivo)
        print(dados['produto'])
        print(dados['preço'])

