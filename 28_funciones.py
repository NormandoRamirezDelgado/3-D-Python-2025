# Definición de una función simple
def saludar():
    print("¡Hola! Bienvenido a Python.")
    print("Esta es una función.")

# Llamada a la función
saludar()
saludar() # Puedes llamarla cuantas veces quieras
print('')

#Parámetros y Argumentos
# 'nombre' es el PARÁMETRO
def saludar_a_alguien(nombre, apellido):
    print(f"¡Hola, {nombre} {apellido}! Qué buen día.")

# "Ana" y "Luis" son los ARGUMENTOS
saludar_a_alguien('Ana', 'Ruiz')
saludar_a_alguien('Luis', 'Vázquez')

print('')
# Esta función recibe dos números y DEVUELVE su suma
def sumar(a, b):
    resultado = a + b
    return resultado

# Llamamos a la función y guardamos el valor que devuelve

total = sumar(5, 3)
print(f"El resultado de la suma es: {total}")
print(f"10 + 15 es: {sumar(10, 15)}")

print('')

