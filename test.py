import tkinter as tk
from tkinter import Button
from Models.NRaphsonMethod import NR_mostrar_tabla

chosseAlg=0
# Función para cambiar la selección de botones
def seleccionar_boton(boton_seleccionado):
    if boton_seleccionado == 'bisec':
        B81.config(bg="red", activebackground="IndianRed1")  # Botón Bisec se selecciona con rojo
        B82.config(bg="SlateGray2", activebackground="SlateGray2")  # Des-seleccionamos el botón Newton
        chosseAlg=1
    elif boton_seleccionado == 'newton':
        B81.config(bg="SlateGray2", activebackground="SlateGray2")  # Des-seleccionamos el botón Bisec
        B82.config(bg="red", activebackground="IndianRed1")  # Botón Newton se selecciona con rojo
        chosseAlg=2
        NR_mostrar_tabla()  # Llamar a la función para mostrar la tabla solo cuando Newton se selecciona


# Crear la ventana principal
root = tk.Tk()
root.title("Selección de Botones")

# Crear un marco para los botones
F = tk.Frame(root)
F.pack(padx=10, pady=10)

# Crear botones y asignarles el comando de selección
B81 = Button(F, text="Bisec", font=("None 25 bold"), bd=4, width=5, bg="SlateGray1", activebackground="IndianRed1", command=lambda: seleccionar_boton('bisec'))
B81.grid(row=8, column=0)

B82 = Button(F, text="Newton", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: seleccionar_boton('newton'))
B82.grid(row=8, column=1)


B83 = Button(F, text="Newton", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: seleccionar_boton('newton'))
B83.grid(row=8, column=1)
# Seleccionar el botón "Bisec" por defecto al iniciar la aplicación
seleccionar_boton('bisec')

# Ejecutar la aplicación
root.mainloop()
