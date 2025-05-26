# Funções que fazem ações no site (abrir, clicar, raspar, etc)
from selenium.webdriver.common.by import By
from .utils import esperar_elemento  # usa a função que centraliza esperas

def abrir_site(driver, url="https://www.coingecko.com/pt"):
    """Abre o site e espera o carregamento do título"""
    driver.get(url)
    esperar_elemento(driver, By.TAG_NAME, "body")  # Espera o corpo da página carregar

def botao_moeda(driver):
    """Abre o seletor de moedas via JS"""
    driver.execute_script('Modal.show("currency_selector")')

def selecionar_moeda_brl(driver):
    """Seleciona o real brasileiro como moeda"""
    elemento = esperar_elemento(driver, By.CSS_SELECTOR, 'div[data-iso-code="brl"]')
    elemento.click()

def selecionar_300_moedas(driver):
    # 1. Clica no botão que abre o menu de opções (por padrão, 100)
    botao_seletor = esperar_elemento(driver, By.CSS_SELECTOR, 'div.gecko-pagination-selector button')
    botao_seletor.click()

    # 2. Clica na opção de 300 moedas (que aparece no menu aberto)
    opcao_300 = esperar_elemento(driver, By.CSS_SELECTOR, 'span[data-url="/pt?items=300"]')
    opcao_300.click()

