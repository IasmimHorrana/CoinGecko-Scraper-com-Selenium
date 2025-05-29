import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Carregar dados do CSV com cache
@st.cache_data
def carregar_dados():
    df = pd.read_csv('../data/dados_cripto.csv', sep=',', decimal='.')

    # Defina apenas as colunas que de fato existem no seu CSV
    colunas_numericas = [
        'Preço',
        'Capitalização de Mercado',
        'FDV',
        'Variação 24h',  # Remova ou comente se não existir
        'Volume'  # Remova ou comente se não existir
    ]
    return df

df = carregar_dados()

# Título e subtítulo
st.title("📊 Dados de Scraping - Criptomoedas (CoinGecko)")
st.subheader("Coletados via Web Scraping no dia 26/05/2025")

# Exibir tabela
st.dataframe(df)
