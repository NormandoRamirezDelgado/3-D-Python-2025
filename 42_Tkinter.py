import tkinter as tk

# Crear una ventana
ventana = tk.Tk()

# Redimensionar la ventana
ventana.geometry('600x480')

# Modificar el título de la ventana
ventana.title('Uso Biblioteca GUI')

# Evitar la redimensión de la ventana
ventana.resizable(0,0)

# Personalizar el color de fondo de la venta
ventana.configure(background="#DBCF88")

# Hacemos visible la ventana
ventana.mainloop()