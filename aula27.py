texto = 'Anotonio flávio vieira da Silva'
novo_texto = ''
for letra in texto:
    if letra == ' ':
        continue

    novo_texto += f'*{letra}'


    print(letra)
print(novo_texto.upper() + '*')

