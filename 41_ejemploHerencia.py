class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def mostrar_info(self):
        return f"{self.marca} {self.modelo} ({self.anio})"
    
    def arrancar(self):
        return "El vehículo está arrancando..."

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas
    
    def mostrar_info(self):  # Sobrescritura de método
        return f"\nAuto: {super().mostrar_info()} - {self.num_puertas} puertas"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindrada):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada
    
    def caballito(self):
        return "\n¡Haciendo caballito! 🏍️\n"

# Uso
auto = Automovil("Toyota", "Corolla", 2023, 4)
moto = Motocicleta("Honda", "CB500", 2022, 500)

print(auto.mostrar_info())
print(auto.arrancar())  # Método heredado
print(moto.caballito())  # Método propio