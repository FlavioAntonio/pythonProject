import os.path

caminho = os.path.join('/home', 'flavio', 'Imagens', 'exemplo')

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo):
        continue
    for imagem in os.listdir(caminho_completo):
        print('   ',caminho_completo+imagem)