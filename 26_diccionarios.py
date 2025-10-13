'''
diccionario_desde_tuplas = dict([('nombre', 'Carlos'), ('edad', 22)])
print(diccionario_desde_tuplas)

print('')
mi_diccionario = {
    "nombre": "Juan",
    'edad'  : 30,
    "ciudad": "Madrid"
}
print(mi_diccionario)
print(mi_diccionario["nombre"])  # Salida: Juan

print('')
print(mi_diccionario.get("profesion"))  # Salida: None
print(mi_diccionario.get("profesion", "No Existe la Llave"))  # Salida: No especificada

print('')
# Modificar un valor existente
mi_diccionario["edad"] = 31

# Añadir un nuevo par clave-valor
mi_diccionario["profesion"] = "Ingeniero"

print(mi_diccionario)
# Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

print('')
claves = mi_diccionario.keys()
print(claves)  # Salida: dict_keys(['nombre', 'edad', 'ciudad', 'profesion'])

print('')
valores = mi_diccionario.values()
print(valores)  # Salida: dict_values(['Juan', 31, 'Madrid', 'Ingeniero'])

print('')
items = mi_diccionario.items()
print(items)  # Salida: dict_items([('nombre', 'Juan'), ('edad', 31), ('ciudad', 'Madrid'), ('profesion', 'Ingeniero')])

print('')
mi_diccionario.pop("ciudad")
#print(ciudad)  # Salida: Madrid
print(mi_diccionario)


#print('')
#borrado = mi_diccionario.popitem()
#print(borrado)
#print(mi_diccionario)

print('')
mi_diccionario.update({"pais": "España", "edad": 32})
print(mi_diccionario)
# Salida: {'nombre': 'Juan', 'edad': 32, 'profesion': 'Ingeniero', 'pais': 'España'}

print('')
for clave in mi_diccionario:
    print(clave, mi_diccionario[clave])

print('')
for clave in mi_diccionario.keys():
    print(clave)

print('')
for valor in mi_diccionario.values():
    print(valor)

print('')
for clave, valor in mi_diccionario.items():
    print(f"La clave es '{clave}' y el valor es '{valor}'")

print('')
programador = {
    "nombre": "Ada", 
    "apellido": "Lovelace", 
    "año_nacimiento": 1815
}
print(len(programador))
# Salida: 3

print('')
configuracion = {
    "host": "localhost", 
    "puerto": 8080
}
config_str = str(configuracion)
print(config_str)
# Salida: "{'host': 'localhost', 'puerto': 8080}"
print(type(config_str))
# Salida: <class 'str'>
'''
print('')
#Cargar valores de manera dinamica en diccionario
diccionarioVacio = {}
for i in range(5):
    llave = input('Introduce la Llave: ')
    valor = input('Introduce el Valor: ')
    diccionarioVacio[llave] = valor

print(diccionarioVacio)

print('')
#Las llaves son: nombre, paterno, materno, edad
diccionarioAlumno = {}
diccionarioAlumno['nombre'] = input('Nombre: ')
diccionarioAlumno['paterno'] = input('Paterno: ')
diccionarioAlumno['materno'] = input('Materno: ')
diccionarioAlumno['edad'] = input('Edad: ')
print(diccionarioVacio)

