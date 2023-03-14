"""

Interpolação basica de strings

s - string
d e i - int
f - float
x e X - hexadecimal

"""

nome = 'Flávio'
preco = 1000.4456544

vari = '%s, o preco é R$%.2f' % (nome, preco)

print(vari)
print(' o hexadeximal de %d é %04X' % (123456789, 123456789))
