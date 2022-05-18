from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

navegador   = wd.Chrome()

#variaveis
urls    = ["https://google.com.br/", "https://www.melhorcambio.com/ouro-hoje#:~:text=O%20valor%20do%20grama%20do,em%20R%24%20300%2C56."]

#Pegando a cotação do dolar
navegador.get(urls[0])
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação do dolar")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacaoDolar    = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacaoDolar)

#Pegando a cotação do euro
navegador.get(urls[0])
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação do euro")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacaoEuro    = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacaoEuro)

#Pegando a cotação do ouro
navegador.get(urls[1])
cotacaoOuro    = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
print(cotacaoOuro)

navegador.quit()

#Importando a tabela de dados
tabela  = pd.read_excel("Produtos.xlsx")
print(tabela)

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"]   = float(cotacaoDolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"]   = float(cotacaoDolar)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"]   = float(cotacaoDolar)
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]


with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(tabela)

tabela.to_excel("NovosProdutos.xlsx", index=False)