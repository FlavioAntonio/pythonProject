numero = input('Digite um numero: ')

try:
    print('STR: ', numero)
    numero_float = float(numero)
    print('Float:', numero_float)
    print(f'O Dobro de {numero} é {numero_float * 2:.2f}')
except:
    print('Isso não é um numero')
