from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
pesoas = [
    'João', 'Joana', 'Luiz', 'Leticia',
]
camisetas = [
    ['preta', 'branca',],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster'],
]

# print_iter(combinations(pesoas, 2))
# print_iter(permutations(pesoas, 2))

print_iter(product(*camisetas))
