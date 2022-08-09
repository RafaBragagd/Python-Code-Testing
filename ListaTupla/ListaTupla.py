'''#Cria uma lista e printa
idades = [20, 39, 18]
print(idades)

#Adiciona o 15 no fim da lista e printa
idades.append(15)
print(idades)

#Adiciona na posição 0 o numero 16 e printa
idades.insert(0, 16)
print(idades)

#Adiciona o 27 e o 19 como valores separados na lista e printa
idades.extend([27, 19])
print(idades)

#Cria uma nova lista somando +1 para cada idade em idades
idades_ano_que_vem = [(idade+1) for idade in idades]
print(idades_ano_que_vem)

#Cria uma lista somando +1 para todas as idades que forem maior que 21
idades2 = [(idade+1) for idade in idades if idade > 21]
print(idades2)

#Cria uma lista com os valores maiores que 21 em idades_ano_que_vem
idades3 = [idade for idade in idades_ano_que_vem if idade > 21]
print(idades3)
'''
#----------------------------------------------------------------------------#
'''
#Cria uma função para printar o tamanho da lista
def faz_processamento_de_visualização(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    #Curiosidade: Não é bom deixar uma lista como valor padrão pois valores
    #adicionados a lista, permanecerão nas proximas chamadas

#cria uma lista, faz uma chamada da função e printa a lista
idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualização(idades)
print(idades)
'''
#-----------------------------------------------------------------------------#
#Funções e tuplas
'''
class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Codigo{self.codigo} saldo {self.saldo}<<]"


conta_do_gui = ContaCorrente(15)
#print(conta_do_gui)

conta_do_gui.deposita(500)
#print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
#print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
    print(conta)

guilherme = ("Guilherme", 37, 1981) #tupla é uma lista imutavel
daniela = ("Daniela", 31, 1987)

print(guilherme, daniela)
'''
#--------------------------------------------------------------------#
#Herança e polimorfismo
from operator import attrgetter
from functools import total_ordering
@total_ordering
class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>Codigo{self._codigo} saldo {self._saldo}<<]"

    def __eq__(self, other):
        if type(other) != Conta:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        else:
            return self._codigo < other._codigo

class ContaCorrente(Conta):
    def __init__(self, codigo):
        super().__init__(codigo)
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def __init__(self, codigo):
        super().__init__(codigo)
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

conta16 = ContaCorrente(16)
conta16.deposita(1500)
#conta16.passa_o_mes()
#print(conta16)

conta19 = ContaCorrente(19)
conta19.deposita(1000)
#conta17.passa_o_mes()
#print(conta17)

conta18 = ContaCorrente(18)
conta18.deposita(2000)

conta17 = ContaCorrente(17)
conta17.deposita(2000)

contas = [conta16, conta17, conta18, conta19]

#def extrai_saldo(conta):
#    return conta._saldo

#contas = sorted(contas, key=extrai_saldo)
#contas = sorted(contas, key=attrgetter("_saldo"))


for conta in sorted(contas):
    print(conta)

#------------------------------------------------------------------------#

idades = [15, 87, 65, 56, 32, 49, 37]
#for i in range(len(idades)):
#    print(f"Indice: {i} | Idade: {idades[i]}")

#for i, idade in enumerate(idades): #enquanto desempacota uma tupla colocar o "_" faz com que ele seja ignorado
#    print(f"Indice: {i} | Idade: {idades[i]}")
'''
print(sorted(idades))
print(sorted(idades, reverse=True))

idades.sort()
print(idades)
idades.sort(reverse=True)
print(idades)
'''