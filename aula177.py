
import os
import json

NOME_ARQUIVO = 'aula177.json'
CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)

filmes = {'title': 'o Senhor dos Anéis: a Sociedade do Anel', 
               'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 
               'is_movie': True, 
               'imdb_rating': 8.8, 
               'year': 2001, 
               'characters': ['Frodo Bolseiro', 
                              'Samwise Gamgee', 
                              'Meriadoc Brandybuck', 
                              'Peregrin Took'], 
               'budget': None}

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(filmes, arquivo, indent=4, ensure_ascii=False)
    

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    print(dados)

