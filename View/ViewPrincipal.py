import tkinter as tk

class ViewPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación Principal")

        self.otra_funcion_button = tk.Button(root, text="Divicion sintetica", font=("Helvetica", 16), padx=20, pady=20)
        self.otra_funcion_button.pack(padx=10, pady=10)
        
        self.calculadora_button = tk.Button(root, text="Biseccion\nNewton R\nGauss S", font=("Helvetica", 16), padx=20, pady=20)
        self.calculadora_button.pack(padx=10, pady=10)

        #self.newton_raphson_button = tk.Button(root, text="Newton Raphson", font=("Helvetica", 16), padx=20, pady=20)
        #self.newton_raphson_button.pack(padx=10, pady=10)