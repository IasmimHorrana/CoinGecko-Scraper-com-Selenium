from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def iniciar_driver():
    options = Options()
    options.add_argument("--ignore-certificate-errors") # options.add_argument("--headless")  # descomente para rodar sem abrir janela
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def main():
    driver = iniciar_driver()
    driver.get("https://www.coingecko.com/pt")
    
    # Espera até que o título contenha "CoinGecko"
    WebDriverWait(driver, 10).until(EC.title_contains("CoinGecko"))
    
    driver.fullscreen_window()
    
    # A partir daqui vai a localização dos elementos, por exemplo:
    # element = driver.find_element(By.CSS_SELECTOR, ".class_do_elemento")
    
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()
