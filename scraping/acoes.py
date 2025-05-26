# Funções que fazem ações no site (abrir, clicar, raspar, etc)
import time
import pandas as pd
import os # Importante para manipulação de arquivos
from selenium.webdriver.common.by import By
from .utils import esperar_elemento  
from .coleta import coletar_dados

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

def botao_next(driver, total_paginas=58):
    todos_dados = []

    for i in range(1, total_paginas + 1):
        print(f"Coletando dados da página {i}...")
        df = coletar_dados(driver)
        if not df.empty:
            todos_dados.append(df)

        try:
            botao_next = esperar_elemento(driver, By.CSS_SELECTOR, 'a[aria-label="next"]')
            botao_next.click()
            time.sleep(3)
        except Exception as e:
            print(f"Erro ao clicar no botão da página {i + 1}: {e}")
            break

    # Junta todos os dados coletados
    resultado = pd.concat(todos_dados, ignore_index=True)

    # Garante que a pasta data exista
    os.makedirs("data", exist_ok=True)

    # Salvando em vários formatos
    resultado.to_csv("data/dados_cripto.csv", index=False)
    resultado.to_parquet("data/dados_cripto.parquet", index=False)
    resultado.to_json("data/dados_cripto.json", orient="records", lines=True)

    print("Dados coletados e exportados com sucesso.")
