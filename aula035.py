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
    },
    {
        'Pergunta': 'Quanto é 10 * 3',
        'Opção': ['54', '15', '30', '1'],
        'Resposta': '5',
    
    },
    {
        'Pergunta': 'Qual a cor do Cavalo brando São pedro',
        'Opção': ['Azul', 'preto', 'Branco', 'Verde'],
        'Resposta': 'Branco',
    
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
        print('Você acertou 👋')
        acerto +=1
        continuar = input('Deseja continuar:❓')
        if continuar == 'não':
            break
    else:
        print('Você errou ❌')

    print()
print(f'Você acertou {acerto} perguntas')
print()