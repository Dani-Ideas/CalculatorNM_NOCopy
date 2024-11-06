#def func( x ):
#    return x * x * x - x * x + 2
#
## Derivative of the above function
## which is 3*x^x - 2*x
#def derivFunc( x ):
#    return 3 * x * x - 2 * x
#
## Function to find the root
#def newtonRaphson( x ):
#    h = func(x) / derivFunc(x)
#    while abs(h) >= 0.0001:
#        h = func(x)/derivFunc(x)
#        # x(i+1) = x(i) - f(x) / f'(x)
#        x = x - h
#    print("The value of the root is : ", "%.4f"% x)
#
## Driver program to test above
#x0 = -20 # Initial values assumed
#newtonRaphson(x0)





import pandas as pd
import tkinter as tk
from tkinter import ttk

# Definir la función
def func(x):
    return x * x * x - x * x + 2

# Derivada de la función
def derivFunc(x):
    return 3 * x * x - 2 * x

# Método de Newton-Raphson modificado para registrar cada iteración
def newtonRaphson(x0):
    iteraciones = []  # Lista para almacenar cada iteración
    h = func(x0) / derivFunc(x0)
    
    while abs(h) >= 0.0001:
        f_x = func(x0)
        f_prime_x = derivFunc(x0)
        h = f_x / f_prime_x
        x_next = x0 - h  # x(i+1)

        # Registrar los datos de la iteración
        iteraciones.append([x0, f_x, f_prime_x, x_next])
        
        # Actualizar el valor de x0 para la siguiente iteración
        x0 = x_next
    
    # Crear un DataFrame con los resultados
    df = pd.DataFrame(iteraciones, columns=['x(i)', 'f(x)', "f'(x)", 'x(i+1)'])
    return df

# Crear la ventana de Tkinter para mostrar la tabla
def mostrar_tabla():
    # Crear ventana
    root = tk.Tk()
    root.title("Tabla de Newton-Raphson")

    # Ejecutar el método de Newton-Raphson y obtener los resultados
    x0 = -20
    df = newtonRaphson(x0)

    # Crear Treeview (tabla)
    tree = ttk.Treeview(root, columns=df.columns.tolist(), show="headings")
    
    # Definir encabezados de columnas
    for col in df.columns:
        tree.heading(col, text=col)

    # Insertar filas en el Treeview
    for _, row in df.iterrows():
        values = list(row)
        tree.insert("", "end", values=values)

    # Ubicar Treeview en la ventana
    tree.pack(padx=10, pady=10)

    # Iniciar el bucle de la interfaz
    root.mainloop()

# Ejecutar la función que muestra la tabla
mostrar_tabla()
