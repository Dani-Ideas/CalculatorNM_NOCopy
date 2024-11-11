import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
from Model.Model_scienceGraficNM import calcular_expresion, sustituir_variable

# Definir la función
def func(x, function):
    result = sustituir_variable(x, function)
    return float(calcular_expresion(result)) 

# Método de bisección modificado
def bisection(a, b, funcionToUse):
    # Comprobación inicial
    if func(a, funcionToUse) * func(b, funcionToUse) >= 0:
        print("Los valores iniciales a y b no cumplen con los requisitos.")
        return
    
    # DataFrame para almacenar resultados
    resultados = []
    
    # Bisección
    while (b - a) >= 0.01:
        # Calcular el punto medio
        c = (a + b) / 2
        # Calcular valores para almacenar en la tabla
        diff_ba = b - a
        new_c = c
        func_c_a = func(c, funcionToUse) * func(a, funcionToUse)
        
        # Añadir la fila de resultados
        resultados.append([a, b, diff_ba, new_c, func_c_a])
        
        # Verificar si c es una raíz
        if func(c, funcionToUse) == 0.0:
            break
        # Actualizar a o b según el criterio
        if func(c, funcionToUse) * func(a, funcionToUse) < 0:
            b = c
        else:
            a = c
    
    # Crear el DataFrame
    df = pd.DataFrame(resultados, columns=['a', 'b', '(b-a)', 'Nuevo c', 'f(c)*f(a)'])
    return df

# Crear la ventana principal de Tkinter
def mb_mostrar_tabla(valuesX, functionX):
    # Convertir valores de entrada a flotantes
    a = float(valuesX[0])
    b = float(valuesX[1])
    
    # Ejecutar el método de bisección y obtener los resultados
    df = bisection(a, b, functionX)

    # Crear ventana
    root = tk.Tk()
    root.title("Tabla de Bisección")

    # Crear Treeview (tabla)
    tree = ttk.Treeview(root, columns=df.columns.tolist(), show="headings")
    
    # Definir encabezados de columnas
    for col in df.columns:
        tree.heading(col, text=col)

    # Insertar filas en el Treeview
    for index, row in df.iterrows():
        values = list(row)
        tree.insert("", "end", values=values)
        
        # Colorear filas según el valor de las celdas
        for i, value in enumerate(values):
            if value < 0:
                tree.tag_configure(f"row_{index}", background="red")
            elif np.isclose(value, 0, atol=1e-6):  # Cerca de 0
                tree.tag_configure(f"row_{index}", background="white")
            else:
                tree.tag_configure(f"row_{index}", background="green")
            tree.item(tree.get_children()[index], tags=(f"row_{index}",))

    # Ubicar Treeview en la ventana
    tree.pack(padx=10, pady=10)

    # Iniciar el bucle de la interfaz
    root.mainloop()
#x**3 - x**2 + 2
#-200
#300