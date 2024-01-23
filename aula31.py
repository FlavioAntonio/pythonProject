def validar_cpf():
    #capiturando o cpf
    cpf = input('Digite seu cpf')

    lista_digitos = cpf[:9]
    contador_1 = 10
    resultado_1 = 0
    for digito in lista_digitos:
        resultado_1 += int(digito) * contador_1
        contador_1 -=1
        digito = (resultado_1 * 10) % 11
        digito = digito if digito <= 9 else 0
    print(digito)
    #segunda parte do codigo

    lista_digitos = cpf[:10] + cpf[0]
    contador_2 = 10
    resultado_2 = 0
    for digito1 in lista_digitos:
        resultado_2 += int(digito1) * contador_2
        contador_2 -= 1
        digito1 = (resultado_2 * 10) % 11
        digito1 = digito1 if digito1 <= 9 else 0
    print(digito1)

validar_cpf()










