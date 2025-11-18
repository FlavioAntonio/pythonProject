from abc import ABC, abstractmethod

class Notificacao:
    def __init__(self, mensagem):
        self.mensagem = mensagem
     
    @abstractmethod    
    def enviar(self):...
    
class NotificacaoEmail(Notificacao):
    def enviar(self):
        print(f'E-mail enviado: ', self.mensagem)
        
n = NotificacaoEmail('Olá, esta é uma notificação por e-mail!')
n.enviar()