
# =================verfificar par ou impar============================
# valor = int(input('digite o valor'))
#
# resto = valor % 2
#
# if resto == 0:
#     print(f'o numero {valor} é PAR')
# else:
#     print(f'o numero {valor} é IMPA')

#===================verificar tamanho do nome====================
nome = input('digite seu nome: ')
tamanho = len(nome)

if tamanho >=1:
    if tamanho <= 4:
        print('seu nome é muito pequeno')
    elif tamanho >= 5 and tamanho <= 6:
        print('seu nome é normal')
    else:
        print("seu nome é muito grande")
else:
    print('digite um valor')



#===================verificar o tempo=================

# hora = float(input('que horas são'))
#
# if hora >= 0 and hora <=12:
#     print('Bom dia ')
# elif hora >= 12.1 and hora <= 17.59:
#     print('Boa tarde')
# elif hora >= 18 and hora <= 23.99:
#     print('Boa noite')
# else:
#     print('hora invalida')
