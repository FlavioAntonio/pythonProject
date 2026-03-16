from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def configurar_driver():
    chrome_options = Options()

    # 1. Configurações úteis para o Chrome
    chrome_options.add_argument("--start-maximized")  # Abre maximizado
    chrome_options.add_argument("--disable-notifications")  # Desativa notificações
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # chrome_options.add_argument("--headless")

    try:
        # 2. Inicializa o driver (o Selenium Manager baixa o driver sozinho)
        driver = webdriver.Chrome(options=chrome_options)
        # Garante que a janela está no tamanho máximo (reforço ao argumento acima)
        driver.maximize_window()

        return driver
    except Exception as e:
        print(f"Erro ao iniciar o Chrome: {e}")
        return None


# Executando
browser = configurar_driver()
browser.get("https://www.google.com")

def scrow_intor_view(driver, elemento):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", elemento)

def pesquisa_google():
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#APjFqb"))).click()
    pesquisa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#APjFqb")))
    pesquisa.send_keys("Documentação do selenium")
    pesquisa.send_keys(Keys.ENTER)

    # clicando na documentação

    wait.until(EC.presence_of_element_located((
        By.XPATH, "//*[text()='O Projeto Selenium de Automação de Navegadores']"))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH,
                                                 "//*[text()='O Projeto Selenium de Automação de Navegadores']")))

    resumo = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Grid")))

    scrow_intor_view(browser, resumo)
    resumo.click()
  
    sleep(10)

pesquisa_google()
