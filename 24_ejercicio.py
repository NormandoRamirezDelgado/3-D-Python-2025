# Hacer un programa que capture 10 elementos enteros y calcule el promedio e imprima cuántos números son menores, mayores e iguales al promedio.

numeros = []
for i in range(10):
    numeros.append(int(input('Número: ')))
promedio = sum(numeros)/10
mayor = []
menor = []
igual = []
for numero in numeros:
    if numero > promedio:
        mayor.append(numero)
    if numero < promedio:
        menor.append(numero)
    if numero == promedio:
        igual.append(numero)
print(f'Fueron {mayor} números Mayores que el Promedio')
print(f'Fueron {menor} números Menores que el Promedio')
print(f'Fueron {igual} números Iguales que el Promedio')
    


