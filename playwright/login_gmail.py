class LogarGmail:
    def __init__(self, page):
        self.page = page


    def realizar_login(self, usuario, senha):
        self.page.goto("https://mail.google.com")
        self.page.get_by_role("textbox", name="E-mail ou telefone").fill(usuario)
        self.page.get_by_role("button", name="Avançar").click()
        self.page.get_by_role("texbox", name="Digite sua senha").fill(senha)
        self.page.get_by_role("button", name="Avançar").click()
