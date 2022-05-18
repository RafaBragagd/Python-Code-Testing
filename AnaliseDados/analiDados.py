import pandas as pd
import plotly.express as px

#Importando e visualizando a base de dados
tabela = pd.read_csv("telecom_users.csv") #Importa os dados do arquivo csv
print(tabela) #Printa a tabela na tela



#Tratando da tabela de dados
tabela  = tabela.drop(["Unnamed: 0"], axis=1)
tabela  = tabela.dropna(how="all", axis=1)
tabela  = tabela.dropna()
print(tabela)

#Calculando dados da tabela
print(tabela["Churn"].value_counts(normalize=True).map('{:.1%}'.format))

#Criando os graficos das colunas
for coluna in tabela.columns:
    if coluna != "IDCliente":
        fig = px.histogram(tabela, x=coluna, color="Churn", color_discrete_sequence=["orange", "purple", "green"])

        fig.show()