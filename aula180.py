import csv 
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula80.csv'

lista_clientes = [
    
    {'Nome': 'Luis Otavio', 'Endereco:': 'Av 1, 22'},
    {'Nome': 'Maria', 'Endereco:': 'Av 2, 33'},
    {'Nome': 'João', 'Endereco:': 'Av 3, 44'}
    
]

with open(CAMINHO_CSV, 'w',) as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo)
    
    for cliente in lista_clientes:
        escritor.writerow(cliente.values())

