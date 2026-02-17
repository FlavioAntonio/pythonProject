from pathlib import Path
PATH_ARQUIVO = Path(__file__).parent / 'log.txt'

class Utilizarios:
    def __init__(self):
        pass
        
    

    def escrever(self, log):
        with open(PATH_ARQUIVO, 'w') as arquivo:
            arquivo.write(log)
            return 'Log escrito com sucesso!'
            
    def ler(self):
        with open(PATH_ARQUIVO, 'r') as arquivo:
            if not PATH_ARQUIVO.exists():
                return 'Arquivo não encontrado.'
            return arquivo.read()

    def gerar_novo_usuario(self):
        prefixo = self.ler()[:3]
        sufixo = self.ler()[3:]
        # converte para inteiro e soma 1
        novo_numero = int(sufixo) + 1
        # formata de volta com zeros a esqueda
        usuario_final = f'{prefixo}{novo_numero:05d}'
        self.escrever(usuario_final)
        return usuario_final


util = Utilizarios()
print(util.gerar_novo_usuario())

        
        
        



