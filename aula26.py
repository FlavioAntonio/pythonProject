nome = input('digite uma frase: ')

tamanho = len(nome)

cont = 0
letra_atual = ''
maior = 0
letra_mas_exibida = ' '

while cont < tamanho:
   letra_atual = nome[cont]

   if letra_atual == ' ':
      cont +=1
      continue
   quant = nome.count(letra_atual)

   if maior < quant:
      maior = quant
      letra_mas_exibida = letra_atual

   cont +=1

print(f'\033[1;30;42m{letra_mas_exibida}\033[m', 'foi exibida', maior)


