import sqlite3
import pandas as pd

# Carrega os dados do CSV
df = pd.read_csv('data/dados_cripto.csv')

# Conecta (ou cria) o banco de dados
conn = sqlite3.connect('dados_cripto.db')

# Exporta os dados para uma tabela chamada 'criptomoedas'
df.to_sql('criptomoedas', conn, if_exists='replace', index=False)

# Fecha conexão
conn.close()

print("✅ Dados importados com sucesso para o SQLite.")
