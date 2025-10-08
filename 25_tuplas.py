# Tupla de números enteros
mi_tupla = (1, 2, 3, 4, 5)

# Tupla con diferentes tipos de datos
tupla_mixta = ("hola", 10, True, 3.14)

# Tupla vacía
tupla_vacia = ()

print('')
# Tupla sin paréntesis (empaquetado de tupla)
otra_tupla = 1, "dos", 3.0

print('')
# Tupla de un solo elemento
tupla_un_elemento = ("uno",)

print('')
mi_lista = [1, 2, 3]
tupla_desde_lista = tuple(mi_lista)
print(mi_lista)
print(tupla_desde_lista)

print('')
mi_tupla = ("manzana", "banana", "cereza")

# Acceder al primer elemento
print(mi_tupla[0])  # Salida: manzana

# Acceder al último elemento con índice negativo
print(mi_tupla[-1]) # Salida: cereza

print('')
mi_tupla = (10, 20, 30, 40, 50, 60)

# Obtener los elementos desde el índice 1 hasta el 3 (sin incluir el 4)
sub_tupla = mi_tupla[1:4]
print(sub_tupla)  # Salida: (20, 30, 40)

print('')
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Salida: (1, 2, 3, 'a', 'b', 'c')

print('')
tupla_base = ("Hola", 10)
tupla_repetida = tupla_base * 3
print(tupla_repetida)  # Salida: ('Hola', 'Hola', 'Hola')

tupla_ = tupla_base + tupla_base + tupla_base + tupla_base
print(tupla_)  # Salida: ('Hola', 'Hola', 'Hola')

print('')
mi_tupla = (1, 2, 3, 2, 4, 2)
print(mi_tupla.count(2))  # Salida: 3

print('')
mi_tupla = ("rojo", "verde", "azul", "verde")
print(mi_tupla.index("verde"))  # Salida: 1

print('')
coordenadas = (1920, 1080)

x, y = coordenadas

print(f"El valor de x es: {x}") # Salida: El valor de x es: 1920
print(f"El valor de y es: {y}") # Salida: El valor de y es: 1080

numeros = (1,2,3,4,5)
for indice, numero in enumerate(numeros):
    print(indice, ' ', numero)

print('')
mi_tupla = ('rojo', 'verde', 'azul', 'verde')
existe_verde = 'verde' in mi_tupla
print(existe_verde)  # Salida: True

print('')
mi_tupla = (10, 20, 30, 50)
print(f"Tupla original: {mi_tupla}")

# 1. Convertir a lista
mi_lista = list(mi_tupla)

# 2. Modificar la lista
mi_lista[2] = 35         # Cambiar un elemento
mi_lista.append(60)      # Añadir un elemento al final
mi_lista.pop(0)          # Eliminar el primer elemento

# 3. Convertir de nuevo a tupla
tupla_modificada = tuple(mi_lista)

print(f"Tupla modificada: {tupla_modificada}")
# Salida: Tupla modificada: (20, 35, 50, 60)

mixta = [1, 2, (3, 4, 5), 3]
print(mixta)
