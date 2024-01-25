import re
import sys


def validar_cpf():
    #capiturando o cpf

    entrada =  input('Digite seu CPF: ')

    cpf = re.sub(
        r'[^0-9]',
        '',
        entrada
    )
    entrada_e_sequencial = entrada == entrada[0] * len(entrada)
    if entrada_e_sequencial:
        print('Você digitou valores sequenciais')
        sys.exit()

    nove_digitos = cpf[:9]
    contador_1 = 10
    resultado_1 = 0
    for digito1 in nove_digitos:
        resultado_1 += int(digito1) * contador_1
        contador_1 -=1
    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    #segunda parte do codigo

    dez_digitos = nove_digitos + str(digito_1)
    contador_2 = 11
    resultado_digito_2 = 0

    for digito2 in dez_digitos:
        resultado_digito_2 += int(digito2) * contador_2
        contador_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
    if cpf_gerado_pelo_calculo == cpf:
        print(f'o cpf: {cpf_gerado_pelo_calculo} é Valido')
    else:
        print(f'o cpf: {cpf_gerado_pelo_calculo} Não é Valido')

validar_cpf()










