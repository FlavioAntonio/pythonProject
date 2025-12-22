import enum


Direcoes = enum.Enum('Direcoes', ['NORTE', 'SUL', 'LESTE', 'OESTE'])

def mover(direcao):
    """Move o personagem na direção especificada."""
    if not isinstance(direcao, Direcoes):
        raise ValueError("Direção inválida.")
    
    print(f'Movendo para {direcao}')


mover(Direcoes.NORTE)
mover(Direcoes.SUL)
mover(Direcoes.LESTE)