import tkinter as tk

class CalculatorView:
    def __init__(self, root):
        self.root = root
         # Obtener las dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Ajustar la ventana a todo el tamaño de la pantalla
        self.root.geometry(f"{int(screen_width*.9)}x{int(screen_height*.8)}")

        # Variables
        self.txt = tk.StringVar()
        self.hidden_frame = tk.Frame(self.root)
        self.create_widgets()

    def create_widgets(self):
        # Frame principal que contiene tanto el Entry principal como los widgets ocultos
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Configurar las columnas para que se expandan proporcionalmente
        self.main_frame.grid_columnconfigure(0, weight=1)  # Primera columna: Entry principal
        self.main_frame.grid_columnconfigure(1, weight=0)  # Segunda columna: Contenedor de widgets ocultos

        # Entry principal (a la izquierda)
        self.entry1 = tk.Entry(self.main_frame, textvariable=self.txt, font=("None 30 bold"), bg="yellow", bd=5)
        self.entry1.grid(row=0, column=0, columnspan=1, pady=10, ipadx=58, ipady=12, sticky="ew")  # Ajuste horizontal

        # Frame con los textos y el segundo Entry (a la derecha)
        self.create_hidden_widgets()

        # Botón para mostrar u ocultar los textos y el segundo Entry
        self.toggle_button = tk.Button(self.main_frame, text="Mostrar/Ocultar", command=self.toggle_hidden_widgets, font=("None 15 bold"))
        self.toggle_button.grid(row=1, column=0, pady=10)

    def create_hidden_widgets(self):
        # Contenedor para el par de textos y el segundo Entry (a la derecha del Entry principal)
        self.hidden_frame = tk.Frame(self.main_frame)
        self.hidden_frame.grid(row=0, column=1, padx=10, sticky="nsew")  # A la derecha

        label1 = tk.Label(self.hidden_frame, text="Texto 1", font=("None 15 bold"), bg="#4A5BEB")
        label1.grid(row=0, column=0)
        label2 = tk.Label(self.hidden_frame, text="Texto 2", font=("None 15 bold"), bg="#4A5BEB")
        label2.grid(row=0, column=1)

        self.entry2 = tk.Entry(self.hidden_frame, font=("None 15 bold"), bg="lightblue", bd=5)
        self.entry2.grid(row=0, column=2)

    def toggle_hidden_widgets(self):
        # Alterna la visibilidad del Frame que contiene los textos y el Entry
        if self.hidden_frame.winfo_ismapped():
            self.hidden_frame.grid_forget()  # Oculta
        else:
            self.hidden_frame.grid(row=0, column=1, padx=10, sticky="nsew")  # Muestra
