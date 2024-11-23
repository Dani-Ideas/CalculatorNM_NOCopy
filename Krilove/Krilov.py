import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def gradiente_conjugado(A, b, tol=1e-6, max_iter=1000):
    """Método de gradiente conjugado para resolver Ax = b"""
    x = np.zeros_like(b)
    r = b - np.dot(A, x)
    p = r.copy()
    rs_old = np.dot(r.T, r)
    res_norms = [np.sqrt(rs_old)]  # Lista para almacenar la norma del residuo en cada iteración
    
    for i in range(max_iter):
        Ap = np.dot(A, p)
        alpha = rs_old / np.dot(p.T, Ap)
        x += alpha * p
        r -= alpha * Ap
        rs_new = np.dot(r.T, r)
        
        res_norms.append(np.sqrt(rs_new))  # Guardar la norma del residuo

        if np.sqrt(rs_new) < tol:
            break
        
        p = r + (rs_new / rs_old) * p
        rs_old = rs_new
    
    return x, i + 1, res_norms

def resolver_sistema():
    try:
        A = eval(entry_matrix.get())
        b = eval(entry_vector.get())
        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float)
        
        if A.shape[0] != A.shape[1] or A.shape[0] != b.shape[0]:
            messagebox.showerror("Error", "La matriz debe ser cuadrada y el tamaño debe coincidir con el vector.")
            return
        
        x, iteraciones, res_norms = gradiente_conjugado(A, b)
        resultado_label.config(text=f"Solución: {x}\nIteraciones: {iteraciones}")
        
        # Graficar la norma del residuo en función de las iteraciones
        plt.figure()
        plt.plot(range(len(res_norms)), res_norms, marker='o')
        plt.yscale('log')
        plt.xlabel('Iteraciones')
        plt.ylabel('Norma del residuo (log)')
        plt.title('Convergencia del método de Gradiente Conjugado')
        plt.grid(True)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Error en la entrada: {e}")

# Interfaz gráfica
root = tk.Tk()
root.title("Método de Gradiente Conjugado")

tk.Label(root, text="Matriz A (en formato de lista de listas):").pack()
entry_matrix = tk.Entry(root, width=50)
entry_matrix.pack()

tk.Label(root, text="Vector b (en formato de lista):").pack()
entry_vector = tk.Entry(root, width=50)
entry_vector.pack()

resolver_btn = tk.Button(root, text="Resolver", command=resolver_sistema)
resolver_btn.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

root.mainloop()

""" Instrucciones:
Ejecuta el programa, aparecerá una ventana con dos campos de texto.
Ingresa la matriz 
𝐴
A como una lista de listas (por ejemplo, [[4, 1], [1, 3]]) y el vector 
𝑏
b como una lista (por ejemplo, [1, 2]).
Haz clic en "Resolver". El programa mostrará la solución del sistema 
𝐴
𝑥
=
𝑏
Ax=b y la cantidad de iteraciones realizadas. """