# Funções que fazem ações no site (abrir, clicar, raspar, etc)

#São usadas juntas para evitar erros causados por páginas que demoram a carregar.
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

def abrir_site(driver, url="https://www.coingecko.com/pt"):
    """Abre o site e espera o carregamento do título"""
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.title_contains("CoinGecko"))
    driver.fullscreen_window()
