import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import altair as alt

# Carregar dados do banco
@st.cache_data
def carregar_dados():
    conn = sqlite3.connect('dados_cripto.db')
    df = pd.read_sql("SELECT * FROM criptomoedas", conn)
    conn.close()
    return df

df = carregar_dados()

st.set_page_config(
    page_title="Dashboard Cripto",
    layout="wide"  # ← Expandir a largura da página
)

# Layout principal
st.title("📊 Análise de Criptomoedas - Snapshot Diário")
st.markdown("Dashboard interativo com base nos dados extraídos do CoinGecko em um único dia.")

aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "📈 Top 10 Moedas do Dia",
    "📈 Top 10 em 7 dias",
    "📉 Maiores Quedas 24h",
    "🔍 Comparador de Moedas",
    "💰 Volume vs Capitalização",
    "⚠️ Radar de Risco x Potencial"
])

