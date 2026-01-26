import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Área de trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

os.makedirs(NOVA_PASTA, exist_ok=True)
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)