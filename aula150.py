from contextlib import contextmanager

@contextmanager
def my_open(caminho_arauivo, modo):
   
    try:
        print('Abrindo o arquivo...')
        arquivo = open(caminho_arauivo, modo)
        yield arquivo
    except Exception as e:
       print(f'Ocorreu um erro: {e}')
    finally:
        arquivo.close()
        print('Arquivo fechado com sucesso!')
    
with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('Fechando o arquivo...')
    