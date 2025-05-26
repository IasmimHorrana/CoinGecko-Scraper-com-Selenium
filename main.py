# Ponto de entrada do projeto (orquestra o que os módulos fazem)

from scraping.driver import iniciar_driver
from scraping.acoes import abrir_site, botao_moeda, selecionar_moeda_brl, selecionar_300_moedas
from scraping.coleta import coletar_dados

def main():
    driver = iniciar_driver()
    abrir_site(driver)
    botao_moeda(driver)
    selecionar_moeda_brl(driver)
    selecionar_300_moedas(driver)

    # Salva o HTML da página carregada
    with open("pagina.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    input("Pressione Enter para fechar o navegador...")
    driver.quit()

if __name__ == "__main__":
    main()

