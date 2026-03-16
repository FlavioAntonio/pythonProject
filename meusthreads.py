from time import sleep
from threading import Thread

""" class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()


    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuThread('Thread 1',2)
t1.start()

for i in range(20):
    print(i)
    sleep(1) """
    

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        
    def comprar(self, quantidade):
        if self.estoque < quantidade:
            print('Não temos ingressos suficietes.')
            return
            
        print(f'Você comprou {quantidade} ingressos. Ainda temos {self.estoque}')
        self.estoque -= quantidade
        
if __name__ == '__main__':
    ingressos = Ingressos(30)
    ingressos.comprar(10)
    ingressos.comprar(30)
        
    