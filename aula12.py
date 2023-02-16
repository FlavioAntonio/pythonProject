name = input('qual é o seu nome: ')
ano_nascimento = int(input('qual é seu ano nascimento: '))
idade = ano_nascimento - 2023
if idade < 18:
    print('você é menor de idade')
    