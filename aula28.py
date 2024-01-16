import os

lista = []
opcao = True

while opcao != 's':
    print('Selecione uma opção')
    opcao = input('[i]Inserir [a]Apagar [l]Listar [S]Sair')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        #tratando possiveis erros
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite numero inteiro')
        except IndexError:
            print('O indice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':

        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('escolha uma i, a ou l')
