class ClasePadre:
    def __init__(self, atributo):
        self.atributo = atributo
    
    def metodo_padre(self):
        print("Método de la clase padre")

class ClaseHija(ClasePadre):
    def __init__(self, atributo, nuevo_atributo):
        super().__init__(atributo)  # Llama al constructor del padre
        self.nuevo_atributo = nuevo_atributo
    
    def metodo_hijo(self):
        print("Método de la clase hija")
    
class ClaseHijo(ClasePadre):
    def __init__(self, atributo, atributoDos, atributoTres):
        super().__init__(atributo)  # Llama al constructor del padre
        # Defino mis atributos locales
        self.atributoDos = atributoDos
        self.atributoTres = atributoTres
    
    def metodo_hijo(self):
        print("Método de la clase hijo")

# Creo la instancia de la clase Hija
hija = ClaseHija('María', 'Pérez')
print(hija.atributo)
print(hija.nuevo_atributo)

print('')
hija.metodo_padre()
hija.metodo_hijo()

# Instancia de Clase Hijo 2
print('')
hijo = ClaseHijo('Pedro', 'Juárez', 'Martínez')
print(hijo.atributo)
print(hijo.atributoDos)
print(hijo.atributoTres)
print('')
hijo.metodo_padre()
hijo.metodo_hijo()

