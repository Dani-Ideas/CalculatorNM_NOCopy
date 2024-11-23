import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp

def metodo_trapecio(funcion, a, b, n):
    """Calcula la integral usando el método del trapecio"""
    x = sp.symbols('x')
    f = sp.lambdify(x, funcion, 'numpy')
    
    h = (b - a) / n
    x_vals = np.linspace(a, b, n + 1)
    y_vals = f(x_vals)
    area = (h / 2) * (y_vals[0] + 2 * sum(y_vals[1:-1]) + y_vals[-1])
    
    return area, x_vals, y_vals

def calcular():
    try:
        funcion = entry_funcion.get()
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())
        
        x = sp.symbols('x')
        area, x_vals, y_vals = metodo_trapecio(funcion, a, b, n)
        
        resultado_label.config(text=f"Área aproximada: {area:.6f}")
        
        # Graficar la función y la aproximación
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, 'b-', label=f"f(x) = {funcion}")
        ax.fill_between(x_vals, y_vals, alpha=0.3, color='lightblue', label="Área aproximada")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Aproximación del Área usando el Método del Trapecio")
        ax.legend()
        
        # Integrar matplotlib con Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
    except Exception as e:
        messagebox.showerror("Error", f"Error en la entrada: {e}")

# Interfaz gráfica
root = tk.Tk()
root.title("Método del Trapecio para Integración")

# Entradas para los parámetros
tk.Label(root, text="Función f(x) (en términos de x):").pack()
entry_funcion = tk.Entry(root, width=40)
entry_funcion.pack()

tk.Label(root, text="Límite inferior (a):").pack()
entry_a = tk.Entry(root, width=20)
entry_a.pack()

tk.Label(root, text="Límite superior (b):").pack()
entry_b = tk.Entry(root, width=20)
entry_b.pack()

tk.Label(root, text="Número de subintervalos (n):").pack()
entry_n = tk.Entry(root, width=20)
entry_n.pack()

# Botón para calcular el área
calcular_btn = tk.Button(root, text="Calcular Área", command=calcular)
calcular_btn.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Marco para el gráfico
frame_grafico = tk.Frame(root)
frame_grafico.pack()

root.mainloop()

""" 
Instrucciones de uso
Ejecuta el programa.
En la interfaz, ingresa la función en términos de x (por ejemplo, x**2 + 3), los límites a y b, y el número de subintervalos n.
Presiona "Calcular Área" para ver la aproximación del área y la gráfica.
Límite inferior 
𝑎
a: Este es el valor donde comienza el intervalo de integración. Por ejemplo, si estás integrando desde 
𝑥
=
0
x=0, pon 0 en 
𝑎
a.

Límite superior 
𝑏
b: Este es el valor donde termina el intervalo de integración. Por ejemplo, si quieres integrar hasta 
𝑥
=
2
x=2, pon 2 en 
𝑏
b.

Número de subintervalos 
𝑛
n: Define la cantidad de subdivisiones del intervalo 
[
𝑎
,
𝑏
]
[a,b] para el método del trapecio. Un número más alto de subintervalos generalmente mejora la precisión. Puedes empezar con un valor como 10 y probar aumentando este número para ver cómo varía el resultado.
Este programa te permitirá visualizar y entender cómo se aproxima el área bajo la curva usando el método del trapecio. """