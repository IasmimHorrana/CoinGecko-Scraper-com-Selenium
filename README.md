# CoinGecko Web Scraping com Selenium

**Objetivo:** Explorar técnicas de **web scraping** utilizando o Selenium, extraindo dados do site [CoinGecko](https://www.coingecko.com/pt), uma referência no acompanhamento de preços de criptomoedas.

## ✅ Funcionalidades Implementadas

- [x] Abertura automática do navegador com Selenium.
- [x] Navegação até a tabela de criptomoedas no CoinGecko.
- [x] Extração de nome, preço e outras informações da tabela principal.
- [x] Armazenamento dos dados em dicionários para manipulação com Python.

## 📌 Tecnologias utilizadas

- Python 3.10+
- Selenium 4.32.0
- Google Chrome (v137)
- ChromeDriver compatível com sua versão do Chrome

---
## 📂 Estrutura de Pastas do Projeto
📁 CoinGecko-Scraper-com-Selenium
- ├── 📁 .git
- ├── 📁 data
- │ └── 📄 dados_cripto.csv
- ├── 📁 scraping
- │ ├── 📄 init.py
- │ ├── 📄 acoes.py
- │ ├── 📄 coleta.py
- │ └── 📄 driver_utils.py
- ├── 📁 venv
- ├── 📄 chromedriver.exe
- ├── 📄 main.py
- ├── 📄 README.md
- ├── 📄 .gitignore
- └── 📄 requirements.txt

### ✅ Descrição rápida dos diretórios:
- `data/`: armazena os dados extraídos.
- `scraping/`: contém os scripts de scraping organizados por responsabilidade.
- `venv/`: ambiente virtual Python.
- `main.py`: script principal de execução.
- `chromedriver.exe`: driver necessário para o Selenium com Chrome.
- `requirements.txt`: bibliotecas necessárias.
- `README.md`: documentação do projeto.

## 🧱 Instalação do Ambiente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/CoinGecko-Scraper-com-Selenium.git
cd CoinGecko-Scraper-com-Selenium
```
### 2. Crie e ative um ambiente virtual
```
python -m venv venv
```
### Ativação Windows
```
venv\Scripts\activate
```
### macOS/Linux
```
source venv/bin/activate
```
### 3. Instale as dependências
```
pip install -r requirements.txt
```
### 4. Configure o ChromeDriver
- Baixe o ChromeDriver compatível com a versão do seu navegador Chrome.
- Coloque o arquivo chromedriver.exe na raiz do projeto (como está feito neste projeto).

### ✅ Pronto! Agora você pode executar o scraper com:
```
python main.py
```

