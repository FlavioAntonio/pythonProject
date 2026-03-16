from playwright.sync_api import sync_playwright

from login_gmail import LogarGmail
from novo_email import NovoEmail

def run():
    with sync_playwright() as pwd:
        browser = pwd.chromium.launch(headless=False)
        context = browser.new_context()
        pagina = context.new_page()

        try:
            login = LogarGmail(pagina)
            login.realizar_login("flaviovieria94@gmail.com", "@Fl@vio@1994@")
            print("Login efetuado com sucesso ✅")
        except Exception as e:
            print(f"Ocorreu um erro durante a execução {e}")

        finally:
            pagina.wait_for_timeout(10)
            browser.close()

if __name__ == "__main__":
    run()