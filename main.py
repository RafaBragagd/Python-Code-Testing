from math import floor
listagem    = [10,50,12,43,98,45,61,75]
Lista       = listagem.copy()
tamanho = len(Lista)
booleano    = tamanho % 2 == 0
Lista.sort()
meio    = int(tamanho/2)
if booleano:
    mediana = Lista[meio-1]
else:
    mediana = Lista[meio]

print(Lista)
print(mediana)