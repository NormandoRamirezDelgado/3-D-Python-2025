# Hacer un programa que calcule el promedio de 10 números enteros e imprima el resultado obtenido
def sumar():
    global suma
    numero = int(input('Introducir el Número Entero: '))
    suma = suma + numero

def promedio():
    promedio = suma / 10
    print('El Promedio de los Números es:',promedio)

suma = 0
for i in range(10):
    sumar()
promedio()