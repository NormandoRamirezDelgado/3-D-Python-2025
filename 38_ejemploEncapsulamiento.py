class Persona:
    def __init__(self):
        self.__nombre = ''
        self.__apellidos = ''
        self.__direccion = ''
    
    # Propiedades Get y Set
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos
    
    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion


# Instanciar la clase
persona = Persona()

# Imprimir el valor Inicial de cada Atributo
print(persona.nombre)
print(persona.apellidos)
print(persona.direccion)

# Asignar valores al atributo mediante Setter
persona.nombre = 'María'
persona.apellidos = 'Ruíz'
persona.direccion = 'Fresno y Ayacahuite'

# Imprimir el valor Inicial de cada Atributo
print(persona.nombre)
print(persona.apellidos)
print(persona.direccion)

# Imprimir el valor de unos atributos concatenandolos
print('\n' + persona.apellidos + ' ' + persona.nombre)