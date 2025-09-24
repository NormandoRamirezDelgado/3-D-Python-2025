#Hacer un programa que calcule el promedio de N números de tipo entero e imprima como resultado el promedio obtenido.
suma = 0
contador = 0
respuesta = 's'
while respuesta.lower() == 's':
    valor = int(input('Introducir un valor entero: '))
    suma += valor  # suma = suma + valor
    contador += 1 # contador = contador + 1
    respuesta = input('Hay más valores s/n?')
promedio = suma / contador
print('El Promedio es: ', promedio)