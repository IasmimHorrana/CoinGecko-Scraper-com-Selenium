import pandas as pd
from io import StringIO
from .utils import esperar_elemento
from selenium.webdriver.common.by import By

def coletar_dados(driver):
    html = StringIO(driver.page_source)
    tabelas = pd.read_html(html, thousands=".", decimal=",", skiprows=1)

    if not tabelas:
        return pd.DataFrame()
    
    df = tabelas[0]

    # Remove linhas totalmente vazias
    df = df.dropna(how="all").reset_index(drop=True)

    # Renomeia colunas
    df.columns = ['Favorito', 'id', 'Moeda', 'Comprar', 'Preço', '1h', '24h', '7d', '30d',
                  'Volume 24h', 'Capitalização de Mercado', 'FDV', 'Cap/FDV', 'Grafico_7dias']

    # Remove colunas desnecessárias
    df.drop(columns=['Favorito', 'Comprar', 'Grafico_7dias'], inplace=True)

    return df