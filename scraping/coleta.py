import pandas as pd
from io import StringIO
from .utils import esperar_elemento
from selenium.webdriver.common.by import By

def coletar_dados(driver):
    html = StringIO(driver.page_source)
    tabelas = pd.read_html(html)
    if tabelas:
        return tabelas[0]
    else:
        return pd.DataFrame()

