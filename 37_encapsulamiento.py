class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular  # Público
        self.__saldo = saldo_inicial  # Privado
        self._movimientos = []  # Protegido
    
    # Método getter
    def obtener_saldo(self):
        return self.__saldo
    
    # Método setter con validación
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            self._movimientos.append(f"Depósito: ${cantidad}")
            return True
        return False
    
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            self._movimientos.append(f"Retiro: ${cantidad}")
            return True
        return False
    
    def mostrar_movimientos(self):
        return self._movimientos.copy()
    
cuenta = CuentaBancaria('María', 100)
print(cuenta.obtener_saldo())
cuenta.depositar(100)
print(cuenta.obtener_saldo())
print(cuenta.mostrar_movimientos())
