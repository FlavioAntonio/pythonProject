import os
from itertools import count


caminho = os.path.join('/home', 'flavio', 'Imagens', 'exemplo')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual:', root)

    for dir_name in dirs:
        print('   ', the_counter, 'Subpasta:', dir_name)

    for file_name in files:
        print('   ', the_counter, 'Arquivo:', caminho + file_name)
