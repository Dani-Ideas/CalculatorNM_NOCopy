import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para calcular el polinomio de Lagrange
def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    total = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        total += term
    return total

# Función para graficar el polinomio de interpolación
def plot_interpolation():
    try:
        x_points = list(map(float, entry_x.get().split(',')))
        y_points = list(map(float, entry_y.get().split(',')))
        if len(x_points) != len(y_points):
            raise ValueError("Las listas de puntos X e Y deben tener la misma longitud.")
        
        # Crear una figura de matplotlib
        fig, ax = plt.subplots()
        x_range = np.linspace(min(x_points) - 1, max(x_points) + 1, 100)
        y_range = [lagrange_interpolation(x_points, y_points, x) for x in x_range]
        
        # Graficar los puntos y el polinomio
        ax.plot(x_range, y_range, label="Polinomio de Lagrange", color="blue")
        ax.scatter(x_points, y_points, color="red", label="Puntos dados")
        ax.legend()
        ax.set_title("Interpolación de Lagrange")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        
        # Mostrar la gráfica en el canvas de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_plot)
        canvas.draw()
        canvas.get_tk_widget().pack()
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Interpolación de Lagrange")

# Entradas para los puntos X e Y
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Puntos X (separados por comas):").grid(row=0, column=0, padx=5, pady=5)
entry_x = tk.Entry(frame_input, width=30)
entry_x.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Puntos Y (separados por comas):").grid(row=1, column=0, padx=5, pady=5)
entry_y = tk.Entry(frame_input, width=30)
entry_y.grid(row=1, column=1, padx=5, pady=5)

# Botón para graficar
button_plot = tk.Button(root, text="Graficar Interpolación", command=plot_interpolation)
button_plot.pack(pady=10)

# Frame para la gráfica
frame_plot = tk.Frame(root)
frame_plot.pack(pady=10)

root.mainloop()
""" En el campo Puntos X, ingresa:

Copiar código
1, 2, 3, 4
En el campo Puntos Y, ingresa:

Copiar código
1, 4, 9, 16 """