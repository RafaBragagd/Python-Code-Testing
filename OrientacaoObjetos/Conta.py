class Conta:
    '''Cria o objeto com os atributos'''
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    '''Metodos direcionados ao saldo'''
    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}.")
    def deposita(self, valor):
        self.__saldo += valor
    def __validar_saldo(self, sacar):
        saldo_disponivel = self.__saldo + self.__limite
        return sacar <= saldo_disponivel
    def saca(self, valor):
        if (self.__validar_saldo(valor)):
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")
    def transfere(self, valor, conta):
        self.saca(valor)
        conta.deposita(valor)
    @property
    def saldo(self):
        return self.__saldo

    '''Metodos direcionados ao titular'''
    @property
    def titular(self):
        return self.__titular.title()

    '''Metodos direcionados ao limite'''
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    '''Medoto direcionados aos codigos do banco'''
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
