#neste bloco é capiturado os dados

name = input('qual é o seu nome: ')
ano_nascimento = int(input('qual é seu ano nascimento: '))
idade = 2023 - ano_nascimento

# this block verifi age the people

if idade < 18:
    print('você é menor de idade')
elif idade > 18 and idade <= 28:
    print ('você é está com meia idade')
elif idade > 28 and idade <= 40:
    print('você já é velho')
    