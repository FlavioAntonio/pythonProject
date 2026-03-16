from playwright.sync_api import sync_playwright
from time import time, sleep

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context() # gerenciar paginas
    # abri o navegador
    pagina = contexto.new_page()

    # navegar na em site

    pagina.goto("https://www.hashtagtreinamentos.com/")


    # selecionar um botão
    botao = pagina.get_by_role("link", name="Confira o que oferecemos para")
    with contexto.expect_page() as pagina2_info:
        botao.click()

    pagina2 = pagina2_info.value
    pagina2.goto("https://www.hashtagtreinamentos.com/treinamentos-corporativos")
    pagina2.get_by_role("textbox", name="*Seu nome").fill("Antonio Flavio")
    pagina2.get_by_role("textbox", name="*Telefone (com DDD)").fill("986089230")
    pagina2.get_by_role("textbox", name="*E-mail corporativo").fill("flaviovieira94@gmail.com")
    pagina2.get_by_role("textbox", name="Nome da empresa").fill("Mdias Branco")

    sleep(2)
    navegador.close()