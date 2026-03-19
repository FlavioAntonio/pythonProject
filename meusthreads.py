from time import sleep
from threading import Thread
from threading import Lock
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
        self.lock = Lock()
        
    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficietes.')
            self.lock.release()
            return
        sleep(1)
        
        print(f'Você comprou {quantidade} ingressos. Ainda temos {self.estoque}')
        self.estoque -= quantidade
        
        self.lock.release()
        
if __name__ == '__main__':
    ingressos = Ingressos(10)
   
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(1,))
        t.start()
        
    print(ingressos.estoque)
        
    