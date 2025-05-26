# Funções que fazem ações no site (abrir, clicar, raspar, etc)

from selenium.webdriver.common.by import By
from .utils import esperar_elemento  # usa a função que centraliza esperas

def abrir_site(driver, url="https://www.coingecko.com/pt"):
    """Abre o site e espera o carregamento do título"""
    driver.get(url)
    esperar_elemento(driver, By.TAG_NAME, "body")  # Espera o corpo da página carregar
    driver.fullscreen_window()

def botao_moeda(driver):
    """Abre o seletor de moedas via JS"""
    driver.execute_script('Modal.show("currency_selector")')

def selecionar_moeda_brl(driver):
    """Seleciona o real brasileiro como moeda"""
    elemento = esperar_elemento(driver, By.CSS_SELECTOR, 'div[data-iso-code="brl"]')
    elemento.click()
