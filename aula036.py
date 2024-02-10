lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Carlos', 'sobrenome': 'Da Silva'},
    {'nome': 'André', 'sobrenome': 'Oliveira'},
    {'nome': 'Pedro', 'sobrenome': 'Martins'},
    {'nome': 'Tiago', 'sobrenome': 'Pereira'},
    {'nome': 'João', 'sobrenome': 'Gold'},
    
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)