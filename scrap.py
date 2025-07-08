import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Configurações do Chrome
options = Options()
options.add_argument('--headless=new')  # Executa em modo headless
options.add_argument('--disable-gpu')  # (opcional) desativa aceleração por hardware
options.add_argument('--no-sandbox')  # (opcional) necessário em alguns ambientes Linux

def obtemDadosB3():

    driver = webdriver.Chrome(options=options)
    url= "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br"
    driver.get(url)

    # Seleciono todas as ações
    chave = driver.find_element(By.XPATH, '//*[@id="selectPage"]/option[4]')
    chave.click()

    # tempo para carregar a pagina
    time.sleep(2)

    # Obtenho as linhas da tabela
    linhas = driver.find_elements(By.XPATH, '//*[@id="divContainerIframeB3"]/div/div[1]/form/div[2]/div/table/tbody/tr')

    # Obtenho as colunas
    dados = []
    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, "td")
        dados.append([coluna.text for coluna in colunas])

    # Fecha o navegador
    driver.quit()

    # Crio as colunas df
    colunas = ["Código", "Ação", "Tipo", "Qtde. Teórica", "Part. (%)"]

    return dados, colunas

    