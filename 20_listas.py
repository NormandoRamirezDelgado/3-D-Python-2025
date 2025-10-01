frutas = ["manzana", "banana", "cereza"]
valor = input('Valor: ')
frutas.append(valor)  # Añade un elemento al final
frutas[1] = "uva"        # Modifica un elemento
print(frutas)            # Salida: ['manzana', 'uva', 'cereza', 'naranja']

print('')
numeros = [1, 2, 3]
numeros_adicionales = [4, 5, 6]
numeros.extend(numeros_adicionales)
print(numeros)

# Salida: [1, 2, 3, 4, 5, 6]

print('')
colores = ["rojo", "verde", "azul"]
colores.insert(1, "amarillo") # Inserta "amarillo" en el índice 1
print(colores)
# Salida: ['rojo', 'amarillo', 'verde', 'azul']

print('')
animales = ["gato", "perro", "pájaro", "perro"]
animales.remove("perro") # Elimina la primera ocurrencia de "perro"
print(animales)
# Salida: ['gato', 'pájaro', 'perro']

print('')
letras = ['a', 'b', 'c', 'd']
letra_eliminada = letras.pop(1) # Elimina el elemento en el índice 1
print(f"Letra eliminada: {letra_eliminada}") # Salida: Letra eliminada: b
print(f"Lista restante: {letras}")   # Salida: Lista restante: ['a', 'c', 'd']

ultimo_elemento = letras.pop() # Elimina el último elemento
print(f"Último elemento: {ultimo_elemento}") # Salida: Último elemento: d
print(f"Lista final: {letras}")      # Salida: Lista final: ['a', 'c']