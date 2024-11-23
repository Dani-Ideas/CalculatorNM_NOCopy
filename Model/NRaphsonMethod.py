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
def nr_mostrar_tabla(val_X, funtionX):
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

 #Ejecutar la función que muestra la tabla
#mostrar_tabla()







#import pandas as pd
#import tkinter as tk
#import sympy as sp
#from tkinter import ttk
#from Model.Model_scienceGraficNM import calcular_expresion, sustituir_variable
#
## Definir la función
#def func(x, function):
#    result = sustituir_variable(x, function)
#    return float(calcular_expresion(result)) 
#
## Derivada de la función
#def derivFunc(x_input, func_input):
#    independient = sp.symbols('x')
#    func_expr = sp.sympify(func_input)
#    resultDerivX = sp.diff(func_expr, independient)
#    result = resultDerivX.subs(independient, x_input)
#    return float(result)
#
## Método de Newton-Raphson modificado para registrar cada iteración
#def newtonRaphson(x0_input, funtionX_input):
#    iteraciones = []
#    
#    # Verificar si la derivada en x0 es cero antes de realizar la primera división
#    f_prime_x = derivFunc(x0_input, funtionX_input)
#    if f_prime_x == 0:
#        print("Error: derivada igual a cero en el primer punto, el método no puede continuar.")
#        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error
#    
#    h = func(x0_input, funtionX_input) / f_prime_x
#    
#    while abs(h) >= 0.0001:
#        f_x = func(x0_input, funtionX_input)
#        f_prime_x = derivFunc(x0_input, funtionX_input)
#        
#        # Verificar si la derivada es cero para evitar división por cero
#        if f_prime_x == 0:
#            print("Error: derivada igual a cero, el método no puede continuar.")
#            break
#
#        h = f_x / f_prime_x
#        x_next = x0_input - h  # x(i+1)
#
#        # Registrar los datos de la iteración
#        iteraciones.append([x0_input, f_x, f_prime_x, x_next])
#
#        # Actualizar el valor de x0 para la siguiente iteración
#        x0_input = x_next
#
#    # Crear un DataFrame con los resultados
#    df = pd.DataFrame(iteraciones, columns=['x(i)', 'f(x)', "f'(x)", 'x(i+1)'])
#    return df
#
## Crear la ventana de Tkinter para mostrar la tabla
#def nr_mostrar_tabla(val_X, funtionX):
#    root = tk.Tk()
#    root.title("Tabla de Newton-Raphson")
#
#    # Ejecutar el método de Newton-Raphson y obtener los resultados
#    x0 = val_X[0]
#    df = newtonRaphson(x0, funtionX)
#
#    if df.empty:
#        print("No se generó la tabla debido a un error.")
#        return
#
#    # Crear Treeview (tabla)
#    tree = ttk.Treeview(root, columns=df.columns.tolist(), show="headings")
#    
#    # Definir encabezados de columnas
#    for col in df.columns:
#        tree.heading(col, text=col)
#
#    # Insertar filas en el Treeview
#    for _, row in df.iterrows():
#        values = list(row)
#        tree.insert("", "end", values=values)
#
#    # Ubicar Treeview en la ventana
#    tree.pack(padx=10, pady=10)
#    root.mainloop()
