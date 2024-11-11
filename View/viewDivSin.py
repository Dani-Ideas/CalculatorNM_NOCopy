import tkinter as tk

class ViewDivSin:
    def __init__(self, root, controller):
        self.root = root  
        self.controller = controller
        self.num_labels_var = tk.StringVar()
        self.setup_ui()

    def setup_ui(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        # Frame contenedor
        self.container = tk.Frame(self.root, bg="#81b29a")
        self.container.pack(fill="both", expand=True)

        # Reloj a la izquierda
        self.clock_label = tk.Label(self.container, fg="#3d405b", bg="#81b29a", font='monospace 14 bold')
        self.clock_label.pack(side="left", padx=10)

        # Texto centrado
        title_label = tk.Label(self.container, text="Calculadora De División Sintética", fg="#3d405b", bg="#81b29a", height=2, font='monospace 24 bold')
        title_label.pack(side="left", expand=True)

        tk.Label(control_frame, text="Escribe el grado de la ecuacion:").pack(side=tk.LEFT, padx=5, pady=5)

        vcmd = (self.root.register(self.controller.validate_numeric_input), '%P')
        entry = tk.Entry(control_frame, textvariable=self.num_labels_var, validate='key', validatecommand=vcmd)
        entry.pack(side=tk.LEFT, padx=5, pady=5)

        tk.Button(control_frame, text="Generar", command=self.controller.create_labels).pack(side=tk.LEFT, padx=5, pady=5)

        self.canvas = tk.Canvas(self.root)
        self.scrollbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def update_clock_label(self, time, date):
        self.clock_label.config(text=f"{time} {date}")


    def update_labels(self, num_labels):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.entries = []

        for i in range(num_labels):  # num_labels es un entero, así que no habrá problema aquí
            label_var = tk.StringVar()
            entry = tk.Entry(self.scrollable_frame, textvariable=label_var, width=5)
            entry.grid(row=0, column=i, padx=5, pady=5)
            self.entries.append(label_var)

        new_button = tk.Button(self.scrollable_frame, text="Calcular", command=self.controller.save_values)
        new_button.grid(row=1, column=0, columnspan=num_labels, pady=10)

        # Frame para mostrar los resultados
        self.result_frame = tk.Frame(self.scrollable_frame)
        self.result_frame.grid(row=2, column=0, columnspan=num_labels)
