class Coche:
    def __init__(self, marca, modelo, color="Blanco"):
        self.marca = marca
        self.modelo = modelo
        self.color = color

# No hace falta pasar el color
autoUno = Coche("Toyota", "Corolla") 

# Aquí sí pasamos el color
autoDos = Coche("Mazda", "3", "Rojo")

print(autoUno.color) # Salida: Blanco
print(autoDos.color) # Salida: Rojo
