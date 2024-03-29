import copy
from aula_project import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1)}
    for p in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
print()
print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')