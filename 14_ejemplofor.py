#Hacer un programa que basado en que en una escuela el promedio mínimo para aprobar la asignatura es de 7, calcule el promedio de la misma con las 10 calificaciones obtenidas durante el parcial. Imprima como resultado si el alumno aprobo o no el curso.
suma = 0
for i in range(10):
    calificacion = float(input(f'Calificación {i + 1}: '))
    suma = calificacion
    promedio = suma / 10
if promedio >= 7:
    print('El Alumno Aprobo el curso')
else:
    print('El Alumno No Aprobo el curso')




