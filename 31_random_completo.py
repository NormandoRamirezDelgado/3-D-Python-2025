import random

# Lista de posibles premios
premios = ['Coche', 'Viaje', 'Nada', 'Gomitas', 'Nada', 'TV']

# 1. Elegir un participante al azar
participantes = ['Juan', 'Ana', 'Miguel', 'Sara']
participante_elegido = random.choice(participantes)
print(f"¡El participante seleccionado es: {participante_elegido}!")

# 2. El participante "lanza un dado" para ver si gana un bonus
lanzamiento = random.randint(1, 6)
print(f"Sacó un {lanzamiento} en el dado.")

if lanzamiento == 6:
    print("¡Felicidades, tienes un bonus!")
else:
    print("No hay bonus esta vez.")

# 3. Asignar un premio al azar de la lista
premio_ganado = random.choice(premios)
print(f"{participante_elegido} ha ganado: ¡{premio_ganado}!")

# 4. Barajar a los participantes para el siguiente turno
random.shuffle(participantes)
print(f"Nuevo orden de participantes: {participantes}")