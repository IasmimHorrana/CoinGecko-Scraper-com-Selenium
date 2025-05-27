import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Conectar ao banco
conn = sqlite3.connect('dados_cripto.db')

# Consulta SQL
query = "SELECT * FROM criptomoedas"
df = pd.read_sql(query, conn)

conn.close()

# Título
st.title("📊 Dashboard de Criptomoedas")

# Exibir os dados
st.dataframe(df)

