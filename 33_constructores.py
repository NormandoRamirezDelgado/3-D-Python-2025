#Definición de la clase

class Persona:
    #Constructor __init__ (dunder - doble underscore)
    def __init__(self, nombre, apellido):
        #Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrarContacto(self):
        print(f'''    Persona:
              Nombre: {self.nombre}
              Apellido: {self.apellido}''')
    

#Creación de Objetos

# Creación de un primer Objeto
personaUno = Persona('Layla', ' Juárez')
personaUno.mostrarContacto()

personaDos = Persona('Pedro', 'Martínez')
personaDos.mostrarContacto()




        
