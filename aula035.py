perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opção': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opção': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opção': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

acerto = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()

    for i, opcao in enumerate(pergunta['Opção']):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    if escolha == pergunta['Resposta']:
        print('Você acertou 😍')
        acerto +=1
        
    else:
        print('Você errou ❌')

    print()
print(f'Você acertou {acerto} perguntas')
print()