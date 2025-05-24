# Define como o navegador é iniciado

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def iniciar_driver():
    """Inicializa o navegador com opções personalizadas"""
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--headless")  # Ative se quiser rodar sem abrir janela
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    return driver
