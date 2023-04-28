nome = input('digite seu nome: ')

tamanho = len(nome)

cont = 0
new_name = ''
while cont < tamanho:
  new_name += f'*{nome[cont]}'

  cont +=1

print(new_name.upper())


