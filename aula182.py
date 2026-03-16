import secrets
import string as s
import os
from colorama import Fore, Style, init
from secrets import SystemRandom as sr

senha = (''.join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=20)))
os.system('clear')
print(f"Senha gerada: {Fore.GREEN}{senha}{Style.RESET_ALL}")

#random = secrets.SystemRandom()

