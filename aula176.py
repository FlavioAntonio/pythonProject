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


string_json = '''
{
    "title": "o Senhor dos Anéis: a Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": [
        "Frodo Bolseiro",
        "Samwise Gamgee",
        "Meriadoc Brandybuck",
        "Peregrin Took"
    ],
    "budget": null
}
'''



data: Movie = json.loads(string_json)
print(data['title'])
print("titulo original do filme " + data['original_title'])
print(data['year'] + 10)
print(data['characters'][2])
print(data['is_movie'])

