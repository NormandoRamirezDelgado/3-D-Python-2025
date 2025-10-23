import random

# Genera un número entre 1 y 10 (incluyendo 1 y 10)
numero = random.randint(1, 10)
print(numero)

# Simular el lanzamiento de un dado de 6 caras
dado = random.randint(1, 6)
print(f"Has sacado un: {dado}")

print('')
# Genera un número entre 0 y 9 (el 10 no se incluye)
numero = random.randrange(30)
print(numero)

# Genera un número par entre 10 y 100 (el 100 no se incluye)
# (10, 12, 14, ..., 98)
numero_par = random.randrange(10, 100, 2)
print(numero_par)

print('')
# Genera un número flotante básico
valor = random.random()
print(valor) # Ejemplo: 0.7386...

print('')
# Genera un número flotante entre 3.5 y 7.2
temperatura = random.uniform(3.5, 7.2)
print(temperatura)

print('')
cartas = ['As', 'Rey', 'Reina', 'Jota']
mi_carta = random.choice(cartas)
print(f"Tu carta es: {mi_carta}")

ganador = random.choice(['Ana', 'Luis', 'Eva'])
print(f"El ganador es: {ganador}")

letra = random.choice('Programación Python')
print(f'La letra elegida es: {letra}')

print('')
numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")

random.shuffle(numeros) # La lista 'numeros' es modificada
print(f"Lista barajada: {numeros}")

print('')
numeros_loteria = range(1, 50) # Números del 1 al 49
ganadores = random.sample(numeros_loteria, 6)
print(f"Los 6 números ganadores son: {ganadores}")

# También funciona con listas
jugadores = ['Carlos', 'Maria', 'Pedro', 'Laura', 'Juan']
equipo = random.sample(jugadores, 3)
print(f"El equipo seleccionado es: {equipo}")

print('')

