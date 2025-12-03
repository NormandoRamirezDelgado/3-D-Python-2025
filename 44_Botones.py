import tkinter as tk
from tkinter import ttk

# Creamos la ventana
ventana  = tk.Tk()
ventana.geometry('600x400')
ventana.resizable(0,0)
ventana.title('Manejo de Etiquetas')
ventana.configure(background='#1D2D44')

# Creamos el Método Saludar
def saludar(nombre):
    print(f'Saludos {nombre}')

# Creación de Botones
boton = ttk.Button(ventana, text='Enviar', command=lambda: saludar('Juan'))
boton.pack(pady=50)

ventana.mainloop()