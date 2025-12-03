import tkinter as tk
from tkinter import ttk

# Creamos la ventana
ventana  = tk.Tk()
ventana.geometry('600x400')
ventana.resizable(0,0)
ventana.title('Manejo de Etiquetas')
ventana.configure(background='#1D2D44')

#Definimos el Método
def mostrar():
    # Recuperar el contenido de la caja de texto
    texto = cajaTexto.get()
    print(f'Texto proporcionado: {texto}')
    etiqueta['text'] = texto


# Definimos la Caja de Texto
cajaTexto = ttk.Entry(ventana, font=('Snell Roundhand', 20))
cajaTexto.pack(pady=50)

# Agregamos un botón
boton = ttk.Button(ventana, text='Enviar', command=mostrar)
boton.pack(pady=50)

# Agregamos una Etiqueta
etiqueta = ttk.Label(ventana, text='Valor Inicial')
etiqueta.pack(pady=50)

ventana.mainloop()