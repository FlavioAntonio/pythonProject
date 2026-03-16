import json
import locale
from pathlib import Path
import string
from datetime import datetime
from colorama import Fore, Style

locale.setlocale(locale.LC_ALL, '')
CAMINHO_ARQUIVO = Path(__file__).parent / 'template.txt'

def converter_para_brl(numero: float) -> str:
    brl = 'R$' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2026, 2, 8)
dados = dict(
    nome='João',
    valor=converter_para_brl(1234.56),
    data=data.strftime('%d/%m/%Y'),
    empresa='Empresa XYZ',
    telefone='(11) 98765-4321'
    
)


texto = '''
Presezado(a) ${nome},
informamos que o valor de ${valor} referente ao serviço contratado em ${data} está disponível para pagamento.
Por favor, entre em contato com nossa equipe pelo telefone ${telefone} para mais informações.
Atenciosamente,
'''

#templete = string.Template(texto)
#print(templete.substitute(dados))

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    conteudo = arquivo.read()
    
    templete = string.Template(conteudo)
    print(templete.substitute(dados))
    