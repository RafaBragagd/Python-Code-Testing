import re

email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone 12345678"
email3 = "1234-1234 é o meu celular"

'''Padrão de busca que será usado no .search() ou do findall'''
padrao = "[0-9]{4,5}[-]*[0-9]{4}"

#retorno = re.search(padrao, email1)
retorno = re.findall(padrao, email2)
print(retorno)