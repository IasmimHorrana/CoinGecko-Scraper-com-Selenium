# Ponto de entrada do projeto (orquestra o que os módulos fazem)

from scraping.driver import iniciar_driver
from scraping.acoes import abrir_site, botao_moeda, selecionar_moeda_brl

def main():
    driver = iniciar_driver()
    abrir_site(driver)
    botao_moeda(driver)
    selecionar_moeda_brl(driver)

    input("Pressione Enter para fechar o navegador...")
    driver.quit()

if __name__ == "__main__":
    main()

