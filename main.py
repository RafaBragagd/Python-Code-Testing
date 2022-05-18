import pandas as pd

tabela = pd.read_excel("webscraping/Produtos.xlsx")
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(tabela)