from abc import ABC, abstractmethod

class Notificacao:
    def __init__(self, mensagem):
        self.mensagem = mensagem
     
    @abstractmethod    
    def enviar(self) -> bool:...
    
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'E-mail enviado: ', self.mensagem)
        return True
        
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f'SMS: enviando:', self.mensagem)
        return False
        
        
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('Notificação enviada com sucesso!')
    else:
        print('falha ao enviar notificação.')
        
notificacao_email = NotificacaoEmail('Testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)