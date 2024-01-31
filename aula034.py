def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

boa_noite = criar_saudacao('Boa noite ')
bom_dia = criar_saudacao('Bom dia ')

lista_nome = ['Flavio', 'Ana', 'Juliane', 'Cassio', 'Marta']
for nome in lista_nome:
    print(bom_dia(nome))
    print(boa_noite(nome))