import os
import pathlib
from string import Template
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

CAMINHO_DO_ARQUIVO = pathlib.Path(__file__).parent / "template.html"

remetente = os.getenv('FROM_EMAIL', '')
password = os.getenv("EMAIL_PASSWORD")

destinatario = remetente
assunto = "Teste de envio de email"
corpo = "Este é um email de teste enviado usando Python."   

# configuraçoes smtp 
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto 

with open(CAMINHO_DO_ARQUIVO, "r") as file:
    texto_arquivo = file.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome="Flavio", 
                                      valor="1.500,00", 
                                      data="30/09/2024", 
                                      telefone="(11) 99999-9999")


# tranformar nossa mensagem em um MIMEMultipart

mime_multpart = MIMEMultipart()
mime_multpart['from'] = remetente
mime_multpart['to'] = destinatario
mime_multpart['subject'] = assunto

corpo_email = MIMEText(texto_email, "html", "utf-8")
mime_multpart.attach(corpo_email)

if not all([smtp_server, smtp_port, smtp_username, smtp_password]):
    print("Configurações SMTP incompletas. Verifique as variáveis de ambiente.")
    print(f"Verifique: SERVER={smtp_server}, PORT={smtp_port}, EMAIL={remetente}")
    exit(1)

# envia o email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(mime_multpart)
        print("Email enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar email: {e}")