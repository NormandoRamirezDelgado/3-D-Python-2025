'''Siustema de Gestión de Estudiantes usando Clases y Constructores en Python'''
class Estudiante:
    def __init__(self, matricula, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula
        self.carrera = carrera
        self.calificaciones = []

    def agregar_calificacion(self, materia, calificacion):
        '''Agrega una calificación a la lista de calificaciones del estudiante'''
        self.calificaciones.append({
            'materia': materia,
            'calificacion': calificacion
        })
    
    def calcularPromedio(self):
        if not self.calificaciones:
            return 0
        
        suma = sum(cal['calificacion'] for cal in self.calificaciones)
        return suma / len(self.calificaciones)
    
    def mostrar_informacion(self):
        '''Muestra la información del estudiante'''
        print(f'{'='*50}')
        print(f'Matrícula: {self.matricula}')
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Carrera: {self.carrera}')
        print(f'\nCALIFICACIONES:')
        if self.calificaciones:
            for cal in self.calificaciones:
                print(f"  Materia: {cal['materia']}, Calificación: {cal['calificacion']}")
            print(f'Promedio: {self.calcularPromedio():.2f}\n')
        else:
            print('No hay calificaciones registradas.')
            print(f'{'='*50}')

#Programa Principal
estudianteUno = Estudiante('2025001', 'Ana Pérez', 20, 'Ingeniería de Sistemas')
estudianteDos = Estudiante('2025002', 'Luis Gómez', 22, 'Medicina')
estudianteTres = Estudiante('2025003', 'María Rodríguez', 19, 'Derecho')

# Agregar Calificaciones a cada estudiante
estudianteUno.agregar_calificacion('Matemáticas', 85)
estudianteUno.agregar_calificacion('Programación', 90)
estudianteUno.agregar_calificacion('Física', 78)

estudianteDos.agregar_calificacion('Anatomía', 88)
estudianteDos.agregar_calificacion('Fisiología', 92)
estudianteDos.agregar_calificacion('Bioquímica', 81)

estudianteTres.agregar_calificacion('Derecho Civil', 75)
estudianteTres.agregar_calificacion('Derecho Penal', 80)
estudianteTres.agregar_calificacion('Derecho Laboral', 70)

# Mostrar Información de cada estudiante
estudianteUno.mostrar_informacion()
estudianteDos.mostrar_informacion()
estudianteTres.mostrar_informacion()

#Comparar Promedios
print('\nCOMPARACIÓN DE PROMEDIOS ENTRE ESTUDIANTES\n')
print(f'{estudianteUno.nombre}: {estudianteUno.calcularPromedio():.2f}')
print(f'{estudianteDos.nombre}: {estudianteDos.calcularPromedio():.2f}')
print(f'{estudianteTres.nombre}: {estudianteTres.calcularPromedio():.2f}')


