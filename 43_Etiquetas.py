import tkinter as tk

# Creamos la ventana
ventana  = tk.Tk()
ventana.geometry('600x400')
ventana.resizable(0,0)
ventana.title('Manejo de Etiquetas')
ventana.configure(background='#1D2D44')

# Creamos una etiqueta
etiqueta = tk.Label(ventana, text='Saludos!')
etiquetaDos = tk.Label(ventana, text='Etiqueta Dos')

# Modificar el texto de la etiqueta
etiqueta.configure(text='Mensaje Nuevo')

# Modifcar el texti de la etiqueta otra forma es:
etiqueta['text'] = 'Último Mensaje'

# Mostrar el componenete Etiqueta
etiqueta.pack(pady=50)
etiquetaDos.pack(pady=100)

ventana.mainloop()