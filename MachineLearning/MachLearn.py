from tkinter import Y
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as lr
from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn import metrics

#Importar a tabela para o python
tabela  = pd.read_csv(r"MachineLearning\advertising.csv")
with pd.option_context('display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(tabela)

#Criar um grafico de calor da correlação da tabela
sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)
plt.show()

#Preparando a tabela para treinar a IA
x   = tabela.drop('Vendas', axis=1)
y   = tabela["Vendas"]

x_train, x_teste, y_train, y_teste  = tts(x, y, test_size=0.2)

#Treinando a IA
lin_reg = lr()
lin_reg.fit(x_train, y_train)

rf_reg  = rfr()
rf_reg.fit(x_train, y_train)

#Testando a IA
test_lin    = lin_reg.predict(x_teste)
test_rf     = rf_reg.predict(x_teste)

r2_lin      = metrics.r2_score(y_teste, test_lin)
rmse_lin    = np.sqrt(metrics.mean_squared_error(y_teste, test_lin))
print(f"r2 da regrassão Linear: {r2_lin}")
print(f"RMSE da regressão Linear: {rmse_lin}")

r2_rf      = metrics.r2_score(y_teste, test_rf)
rmse_rf    = np.sqrt(metrics.mean_squared_error(y_teste, test_rf))
print(f"r2 da Random Forest: {r2_rf}")
print(f"RMSE da Random Forest: {rmse_rf}")

#Analise grafica dos testes
tabela_res  = pd.DataFrame()

tabela_res['y_teste'] = y_teste
tabela_res['Previsão_Rf'] = test_rf
tabela_res["Previsão_Lin"] = test_lin
tabela_res  = tabela_res.reset_index(drop=True)

fig     = plt.figure(figsize=(15,5))
sns.lineplot(data=tabela_res)
plt.show()

feature     = pd.DataFrame(rf_reg.feature_importances_, x_train.columns)
plt.figure(figsize=(5,5))
sns.barplot(x=feature.index, y=feature[0])
plt.show()

#deploy
novos   = pd.read_csv(r"MachineLearning\novos.csv")
novos["Vendas"] = rf_reg.predict(novos)
print(novos)