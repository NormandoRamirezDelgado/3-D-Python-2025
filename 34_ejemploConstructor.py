class Aritmetica:
    def __init__(self, operandoUno, operandoDos):
        self.operandoUno = operandoUno
        self.operandoDos = operandoDos
    
    def sumar(self):
        resultado = self.operandoUno + self.operandoDos
        print(f'El Resultado de la suma: {resultado}')
    
    def restar(self):
        resultado = self.operandoUno - self.operandoDos
        print(f'El Resultado de la resta: {resultado}')

    def multiplicar(self):
        resultado = self.operandoUno * self.operandoDos
        print(f'El Resultado de la multiplicación: {resultado}')

    def dividir(self):
        resultado = self.operandoUno / self.operandoDos
        print(f'El Resultado de la división: {resultado}')
    
print('*** Ejemplo Clase Aritmética ***')
aritmeticaUno = Aritmetica(7, 12)
aritmeticaUno.sumar()
aritmeticaUno.restar()
aritmeticaUno.multiplicar()
aritmeticaUno.dividir()

print()
operandoUno = int(input('Valor entero: '))
operandoDos = int(input('Valor entero: '))
aritmeticaDos = Aritmetica(operandoUno, operandoDos)
aritmeticaDos.sumar()
aritmeticaDos.restar()
aritmeticaDos.multiplicar()
aritmeticaDos.dividir()
    



