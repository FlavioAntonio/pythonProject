import random
from zipfile import Path
from colorama import Fore, Style, init

historico = []
cont = 10
i = 0
while i < 10:
    input("Pressione Enter para gerar um número aleatório...")
    numero = random.randint(1, 100)
    
    if numero not in historico:
        
        historico.append(numero)
        print(f"{Fore.GREEN}Número gerado: {numero}")
        print(f"{Fore.YELLOW}Histórico: {historico}")
        i += 1
    else:
        print(f"{Fore.RED}Número repetido: {numero}. Gerando outro número... ")
        
    print(f"{Fore.CYAN}Total de números únicos gerados: {(historico)}")