entra = input('vc quer entrar ? S/N')
senha_digitada = int(input('digite a senha: '))
senha = 123456
if entra == 'S' or entra == 's' and senha == senha_digitada:
    print('logado com sucesso')
elif entra == 'n' or entra == 'N':
    print('Obrigado por usar nossos serviços')
else:
    print('usuario ou senha invalidos')