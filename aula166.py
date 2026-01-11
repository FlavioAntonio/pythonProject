from datetime import date, datetime

class Aniversario:

    def calcalar_idade(self):
        entrada = input('Digite sua data de nascimento (dd/mm/aaaa): ')
        data_nascimento = datetime.strptime(entrada, "%d/%m/%Y").date()
        hoje = date.today()

        idade = hoje.year - data_nascimento.year
        if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        proximo_aniversario = date(hoje.year, data_nascimento.month, data_nascimento.day)
        if proximo_aniversario < hoje:
            proximo_aniversario = date(hoje.year + 1, data_nascimento.month, data_nascimento.day)

        dias_ate_aniversario = (proximo_aniversario - hoje).days

        print(f'Você tem {idade} anos.')
        print(f'Faltam {dias_ate_aniversario} dias para o seu próximo aniversário.')
        print(f'Seu próximo aniversário será em {proximo_aniversario.strftime("%d/%m/%Y")}.')


aniversario = Aniversario()
aniversario.calcalar_idade()
