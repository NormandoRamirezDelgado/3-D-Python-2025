'''Hacer un programa que pida la edad e una persona e imprima como resultado si es mayor de edad y su año de nacimiento'''
edad = int(input('Cual es tu edad? '))

if edad >= 18:
    print('Es mayor de edad')
    nacimiento = 2025 - edad
    print('El año de nacimiento es: ', nacimiento)

