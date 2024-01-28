salas = [
    ['Maria', 'Elena', ],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduarda'],
]

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)