nome = input('Qual é o seu nome: ')
idade = input('qual é a sua idade: ')

qt = len(nome)

if nome != '' and idade != '':
    print(f'seu nome é {nome}')
    print(f'sua idade é {idade}')
    print(f' seu nome invertido é {nome[::-1]}')
    print(f'seu nome contem {len(nome)} letras')
    print(f'seu nome contem eapaços ', " " in nome)
    print(f' a primeira letra do seu nome é {nome[0]}')
    qt = qt -1
    print(f'a ultima letra do seu nome é: {nome[qt]}')
else:
    print('Você não digitou nada')
