

v1 = int(input('digite um valor: '))
v2 = int(input('digite outro valor: '))

#verificando qual é o maior numvero
if v1 > v2:
    v3 = v1
    print(f'o valor {v1} é mario que o {v2}')
elif v2 > v1:
    v3 = v2
    print(f'o valor {v2} é maior que {v1}')
else:
    print(f'o valores {v1} e {v2}são iguais')