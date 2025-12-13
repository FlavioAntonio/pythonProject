class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
        
    def __enter__(self):
        print('Abrindo o arquivo...')
        self._arquivo = open(self.caminho_arquivo, self.modo)
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando o arquivo...')
        return self._arquivo.close()
    
with MyOpen('aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

