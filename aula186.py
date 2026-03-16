import os
import shutil
from pathlib import Path
from zipfile import ZipFile


CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'arquivos.zip'
CAMINHO_COMPACATADO = CAMINHO_RAIZ / 'compacatado.zip'
CAMINHO_EXTRAIDO = CAMINHO_RAIZ / 'extraido'

CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = f'Arquivo {i}'
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)
            
criar_arquivos(10, CAMINHO_ZIP_DIR)

with ZipFile(CAMINHO_COMPACATADO, 'w') as zip_file:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip_file.write(os.path.join(root, file), file)


with ZipFile(CAMINHO_COMPACATADO, 'r') as zip_file:
    zip_file.extractall(CAMINHO_EXTRAIDO)
