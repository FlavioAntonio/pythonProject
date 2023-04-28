#=================Calculadora======================

valor = int(input('digite o valor da tabuada: '))
condicao = int(input('você quer +[1], /[2] *[3] -[4]: '))



cont = 1
while cont <= 10:

    if condicao == 1:

        resultado = valor + cont
        print(f'{valor} + {cont} = {resultado:.0f}')
    elif condicao == 2:

        resultado = valor / cont

        print(f'{valor} / {cont} = {resultado:.1f}')
    elif condicao == 3:

        resultado = valor * cont
        print(f'{valor} * {cont} = {resultado:.0f}')
    elif condicao == 4:

        resultado = valor - cont
        print(f'{cont} - {valor} = {resultado:.0f}')
    else:
        print('valor invalido')
    cont +=1
