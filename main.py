# Ponto de entrada do projeto (orquestra o que os módulos fazem)

from scraping.driver import iniciar_driver
from scraping.acoes import abrir_site

def main():
    driver = iniciar_driver()
    abrir_site(driver)

    # Aqui adiciona outras ações do scraping

    input("Pressione Enter para fechar o navegador...")
    driver.quit()

if __name__ == "__main__":
    main()

