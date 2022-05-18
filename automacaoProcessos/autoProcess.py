import pyautogui as ag
from pyperclip import copy as cp
import pandas as pd

from time import sleep
#variaveis
linkTab     = "https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh"
pathArq     = r"C:\Users\rafae\Downloads\Vendas - Dez.xlsx"
linkEmail   = "https://mail.google.com/mail/u/0/?tab=om#inbox"
usuarios    = ["Rafael Braga"]
tituloEmail = "Relátorio de vendas"
tempo       = 10
#configuração
ag.PAUSE = tempo
#Acessar o navegador
ag.press("win") #precione a tecla win
ag.write("Navegador") #escreva "Navegador"
ag.press("enter") #precione enter
sleep(tempo) #espera 5 segundos

#Copiar o link e acessar o drive
cp(linkTab) #copie o link na area de transferencia
ag.hotkey("ctrl", "v") #Precione ctrl+v
ag.press("enter") #Precione o enter

#Baixar o arquivo do drive
ag.click(x=406, y=384) #Clica no documento
ag.click(x=1157, y=189) #Clica nas opções do documento
ag.click(x=972, y=591) #Seleciona download
sleep(tempo*8)

#Importar a tabela para o python e processar as informações
tabela = pd.read_excel(pathArq) #importa a tabela Vendas - Dez
print(tabela)

faturamento = tabela["Valor Final"].sum() #Soma o valor da coluna Valor Final
quantidade  = tabela["Quantidade"].sum() #Soma o valor da coluna Quantidade

texto       = (f"O faturamento total foi de: {faturamento:,.2f}.\n "
               f"A quantidade de produtos vendidos foi de: {quantidade:,}.") #texto com o faturamento e a quatidade

#Abre o email e a janela de criação de emails
ag.hotkey("ctrl", "t") #Abre uma nova aba
ag.click(x=454, y=44) #Clica na navegação
cp(linkEmail) #Copia o link do email
ag.hotkey("ctrl", "v") #Cola o link do email
ag.press("enter") #Aperta a tecla enter
sleep(tempo*2)
ag.click(x=137, y=201) #clica no botão "Escrever"

#Escreve e envia o email
for user in usuarios:#Cria um loop para adicionar todos os usuarios
    cp(user) #Copia o nome do usuario que será mandado o email
    ag.hotkey("ctrl", "v") #Cola o nome do usuario
    ag.press("enter") #preciona enter para selecionar o usuario

ag.press("tab") #Preciona tab para ir para o proximo campo
cp(tituloEmail) #Copia o titulo do email
ag.hotkey("ctrl", "v") #Cola o titulo do email
ag.press("tab") #Preciona tab para ir para o proximo campo
cp(texto) #Copia o texto do email
ag.hotkey("ctrl", "v") #Cola o texto do email
ag.hotkey("ctrl", "enter")#envia o email








