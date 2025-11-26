class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__deposito = 0
    
    @property
    def saldo(self):
        """Obtiene el saldo actual"""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, cantidad):
        self.__saldo = cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, valor):
        self.__titular = valor
    
    @property
    def deposito(self):
        return self.__deposito

    @deposito.setter
    def deposito(self, deposito):
        self.__saldo = self.__saldo + deposito
    


# Uso
titular = input('Nombre del Cliente: ')
deposito = float(input('Deposito Inicial: $'))
cuenta = CuentaBancaria(titular, deposito)
print(cuenta.saldo)     # 1000
cuenta.deposito = 1500     # OK
print(cuenta.saldo)


