import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp

def metodo_simpson_38(funcion, a, b, n):
    """Calcula la integral usando el método de Simpson 3/8"""
    if n % 3 != 0:
        raise ValueError("El número de subintervalos debe ser múltiplo de 3 para Simpson 3/8.")
    
    x = sp.symbols('x')
    f = sp.lambdify(x, funcion, 'numpy')
    
    h = (b - a) / n
    x_vals = np.linspace(a, b, n + 1)
    y_vals = f(x_vals)
    area = (3 * h / 8) * (y_vals[0] + 3 * sum(y_vals[1:-1:3]) + 3 * sum(y_vals[2:-1:3]) + 2 * sum(y_vals[3:-3:3]) + y_vals[-1])
    
    return area, x_vals, y_vals

def calcular():
    try:
        funcion = entry_funcion.get()
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())
        
        if n % 3 != 0:
            messagebox.showerror("Error", "El número de subintervalos debe ser múltiplo de 3.")
            return
        
        x = sp.symbols('x')
        area, x_vals, y_vals = metodo_simpson_38(funcion, a, b, n)
        
        resultado_label.config(text=f"Área aproximada: {area:.6f}")
        
        # Graficar la función y la aproximación
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, 'b-', label=f"f(x) = {funcion}")
        ax.fill_between(x_vals, y_vals, alpha=0.3, color='lightcoral', label="Área aproximada")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Aproximación del Área usando el Método de Simpson 3/8")
        ax.legend()
        
        # Integrar matplotlib con Tkinter
        for widget in frame_grafico.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
    except Exception as e:
        messagebox.showerror("Error", f"Error en la entrada: {e}")

# Interfaz gráfica
root = tk.Tk()
root.title("Método de Simpson 3/8 para Integración")

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

tk.Label(root, text="Número de subintervalos (múltiplo de 3, n):").pack()
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
En la interfaz:
Ingresa la función en términos de x (por ejemplo, x**2 + 3).
Ingresa el límite inferior a y el límite superior b.
Ingresa un número múltiplo de 3 para los subintervalos n (por ejemplo, 9).
Presiona "Calcular Área" para ver el área aproximada y la gráfica.
 """