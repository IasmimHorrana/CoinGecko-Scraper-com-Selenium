from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def esperar_elemento(driver, by, seletor, timeout=5):
    """Espera até que o elemento esteja clicável e o retorna"""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, seletor))
    )

