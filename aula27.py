
palavra_secreta = 'perfume'
letras_acetadas = ''

while True:
    letra_digitada = input('digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra. ')
        continue

    if letra_digitada in palavra_secreta:
        letras_acetadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acetadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

