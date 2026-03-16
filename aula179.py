from pathlib import Path
import csv
CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

print(CAMINHO_CSV)


with open(CAMINHO_CSV, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    #next(leitor_csv)  # Pula o cabeçalho
    
    for linha in leitor_csv:
        print(linha)