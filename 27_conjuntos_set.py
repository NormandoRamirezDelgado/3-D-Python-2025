# Creación de un conjunto de números
numeros = {1, 2, 3, 4, 5}
print(numeros)

# Creación de un conjunto de cadenas
frutas = {"manzana", "banana", "naranja"}
print(frutas)

print('')
# Creación de un conjunto a partir de una lista (eliminará duplicados)
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
conjunto_desde_lista = set(lista_con_duplicados)
print(conjunto_desde_lista)  # Salida: {1, 2, 3, 4, 5}

# Creación de un conjunto a partir de una cadena
conjunto_desde_cadena = set("hola a todos")
print(conjunto_desde_cadena)

print('')
# Añade un elemento al conjunto. Si el elemento ya existe, no se produce ningún cambio.
mi_conjunto = {1, 2, 3}
mi_conjunto.add(4)
print(mi_conjunto)  # Salida: {1, 2, 3, 4}

# Elimina un elemento del conjunto. Si el elemento no existe, se generará un error KeyError.
mi_conjunto.remove(2)
print(mi_conjunto)  # Salida: {1, 3, 4}

# Elimina un elemento del conjunto. Si el elemento no existe, no se produce ningún error.
mi_conjunto.discard(5) # No genera error
print(mi_conjunto)  # Salida: {1, 3, 4}

# Elimina y devuelve un elemento arbitrario del conjunto.
print('Método pop: ', mi_conjunto.pop())


print('')
# Devuelve el número de elementos en el conjunto.
print(len(mi_conjunto))

print('')
# Comprueba si un elemento existe en el conjunto. Devuelve True o False.
print( 8 in mi_conjunto )
if 8 in mi_conjunto:
    print('El número 8 está en el conjunto')
else:
    print('El número 8 NO está en el conjunto')

print('')
# frozenset, que es una versión inmutable de un conjunto.
valores = frozenset([1, 3])
print(valores)

print('')
# Elimina todos los elementos del conjunto.
numeros = {1, 2, 3, 4, 5}
numeros.clear()
print(numeros)


