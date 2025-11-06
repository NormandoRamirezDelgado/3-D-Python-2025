#Definición de una Clase
class Persona:
    def inicializarPersona(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrarPersona(self):
        print('- - - Persona - - -')
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')

#Creación de Objetos
persona = Persona() #Crear una Instancia de Persona "Objeto"
nombre = input('Nombre ')
apellido = input('Apellido ')
persona.inicializarPersona(nombre, apellido)
persona.mostrarPersona()


personaDos = Persona() #Crear una Instancia de Persona "Objeto"
personaDos.inicializarPersona('Pedro', 'Juarez')
personaDos.mostrarPersona()

persona.mostrarPersona()

