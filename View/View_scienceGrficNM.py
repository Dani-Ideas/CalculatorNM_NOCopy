import tkinter as tk

class CalculatorView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        # Obtener las dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{int(screen_width * .9)}x{int(screen_height * .8)}")
        self.txt = tk.StringVar()
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

        # Frame 2: Botones y botón para mostrar/ocultar
        self.frame2 = tk.Frame(self.main_frame)
        self.frame2.grid(row=1, column=0, sticky="nsew")

        # Crear los botones de la calculadora
        self.create_buttons(self.frame2)

    def create_buttons(self, frame):
        self.B11 = tk.Button(frame, text="sin", command=lambda: self.controller.press("sin("), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B11.grid(row=1, column=0)
        self.B12 = tk.Button(frame, text="cos", command=lambda: self.controller.press("cos("), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B12.grid(row=1, column=1)
        self.B13 = tk.Button(frame, text="tan", command=lambda: self.controller.press("tan("), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B13.grid(row=1, column=2)
        self.B14 = tk.Button(frame, text="log", command=lambda: self.controller.press("log("), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B14.grid(row=1, column=3)
        self.B15 = tk.Button(frame, text="Clear", command=self.controller.reset, font=("None 25 bold"),bd=4, width=5, bg="tomato", activebackground="red")
        self.B15.grid(row=1, column=4)

        self.B21 = tk.Button(frame, text="pow", command=lambda: self.controller.press("**"), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B21.grid(row=2, column=0)
        self.B22 = tk.Button(frame, text="sqrt", command=lambda: self.controller.press("sqrt"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B22.grid(row=2, column=1)
        self.B23 = tk.Button(frame, text="exp", command=lambda: self.controller.press("exp"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B23.grid(row=2, column=2)
        self.B24 = tk.Button(frame, text="log10", command=lambda: self.controller.press("log10"), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B24.grid(row=2, column=3)
        self.B25 = tk.Button(frame, text="Del", command=self.cancel, font=("None 25 bold"),bd=4, width=5, bg="#57596B", activebackground="goldenrod1")
        self.B25.grid(row=2, column=4)

        self.B31 = tk.Button(frame, text="sinh", command=lambda: self.controller.press("sinh"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B31.grid(row=3, column=0)
        self.B32 = tk.Button(frame, text="cosh", command=lambda: self.controller.press("cosh"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B32.grid(row=3, column=1)
        self.B33 = tk.Button(frame, text="tanh", command=lambda: self.controller.press("tanh"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B33.grid(row=3, column=2)
        self.B34 = tk.Button(frame, text="Deg", command=lambda: self.controller.press("degrees"), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B34.grid(row=3, column=3)
        self.B35 = tk.Button(frame, text="Rad", command=lambda: self.controller.press("radians"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B35.grid(row=3, column=4)

        self.B41 = tk.Button(frame, text="7", command=lambda: self.controller.press("7"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B41.grid(row=4, column=0)
        self.B42 = tk.Button(frame, text="8", command=lambda: self.controller.press("8"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B42.grid(row=4, column=1)
        self.B43 = tk.Button(frame, text="9", command=lambda: self.controller.press("9"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B43.grid(row=4, column=2)
        self.B44 = tk.Button(frame, text="*", command=lambda: self.controller.press("*"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
        self.B44.grid(row=4, column=3)
        self.B45 = tk.Button(frame, text="/", command=lambda: self.controller.press("/"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
        self.B45.grid(row=4, column=4)

        self.B51 = tk.Button(frame, text="4", command=lambda: self.controller.press("4"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B51.grid(row=5, column=0)
        self.B52 = tk.Button(frame, text="5", command=lambda: self.controller.press("5"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B52.grid(row=5, column=1)
        self.B53 = tk.Button(frame, text="6", command=lambda: self.controller.press("6"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B53.grid(row=5, column=2)
        self.B54 = tk.Button(frame, text="+", command=lambda: self.controller.press("+"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
        self.B54.grid(row=5, column=3)
        self.B55 = tk.Button(frame, text="-", command=lambda: self.controller.press("-"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
        self.B55.grid(row=5, column=4)

        self.B61 = tk.Button(frame, text="1", command=lambda: self.controller.press("1"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B61.grid(row=6, column=0)
        self.B62 = tk.Button(frame, text="2", command=lambda: self.controller.press("2"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B62.grid(row=6, column=1)
        self.B63 = tk.Button(frame, text="3", command=lambda: self.controller.press("3"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B63.grid(row=6, column=2)
        self.B64 = tk.Button(frame, text="(", command=lambda: self.controller.press("("), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue1")
        self.B64.grid(row=6, column=3)
        self.B65 = tk.Button(frame, text=")", command=lambda: self.controller.press(")"), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue1")
        self.B65.grid(row=6, column=4)

        self.B71 = tk.Button(frame, text="π", command=lambda: self.controller.press("pi"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B71.grid(row=7, column=0)
        self.B72 = tk.Button(frame, text="0", command=lambda: self.controller.press("0"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B72.grid(row=7, column=1)
        self.B73 = tk.Button(frame, text=".", command=lambda: self.controller.press("."), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B73.grid(row=7, column=2)
        self.B74 = tk.Button(frame, text="e", command=lambda: self.controller.press("e"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B74.grid(row=7, column=3)
        #B75 = tk.Button(frame, text="Redy", command=cal, font=("None 25 bold"),bd=4, width=5, bg="lime", activebackground="cyan")
        #B75.grid(row=7, column=4)

        self.B75 = tk.Button(frame, text="Redy", command=self.controller.calculate, font=("None 25 bold"),bd=4, width=5, bg="lime", activebackground="cyan")
        self.B75.grid(row=7, column=4)

        self.B81 = tk.Button(frame, text="Bisec", font=("None 25 bold"), bd=4, width=5, bg="SlateGray1", activebackground="IndianRed1", command=lambda: self.controller.chosseMN(1))
        self.B81.grid(row=8, column=0)
        self.B82 = tk.Button(frame, text="Newton", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: self.controller.chosseMN(2))
        self.B82.grid(row=8, column=1)
        self.B83 = tk.Button(frame, text="Gauss.E", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: self.controller.chosseMN(3))
        self.B83.grid(row=8, column=2)
        self.B84 = tk.Button(frame, text="Lagrange", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: self.controller.chosseMN(4))
        self.B84.grid(row=8, column=3)

        self.B85 = tk.Button(frame, text="X", command=lambda: self.controller.press("X"),font=("None 25 bold"), bd=4, width=5, bg="gray", activebackground="lightgray")
        self.B85.grid(row=8, column=4)
        
        # Botón para mostrar/ocultar los widgets
        #self.toggle_button = tk.Button(frame, text="Mostrar/Ocultar", command=self.toggle_hidden_widgets, font=("None 15 bold"))
        #self.toggle_button.grid(row=9, columnspan=15, pady=10)

    def create_hidden_widgets(self):
        # Contenedor para el par de textos y el segundo Entry (a la derecha del Entry principal)
        self.hidden_frame = tk.Frame(self.main_frame)
        self.hidden_frame.grid(row=0, column=1, padx=10, sticky="nsew")  # A la derecha

        # Etiquetas y Entry oculto
        self.label1 = tk.Label(self.hidden_frame, font=("None 15 bold"), bg="#4A5BEB")
        self.label1.grid(row=0, column=0)
        self.entry2 = tk.Entry(self.hidden_frame, font=("None 15 bold"), bg="lightblue", bd=5)
        self.entry2.grid(row=0, column=1)
        self.label2 = tk.Label(self.hidden_frame, font=("None 15 bold"), bg="#4A5BEB")
        self.label2.grid(row=0, column=3)
        self.entry3 = tk.Entry(self.hidden_frame, font=("None 15 bold"), bg="lightblue", bd=5)
        self.entry3.grid(row=0, column=4)

    def toggle_hidden_widgets(self):
        if self.hidden_frame.winfo_ismapped():
            self.hidden_frame.grid_forget()  # Oculta
        else:
            self.hidden_frame.grid(row=0, column=1, padx=10, sticky="nsew")  # Muestra

    def get_valueX(self):
        values = []
        if self.entry2.get():
            values.append(self.entry2.get())
        if self.entry3.get():
            values.append(self.entry3.get())
        return values  

    def set_text(self, text):
        self.txt.set(text)

    def get_text(self):
        return self.txt.get()
    
    def cancel(self):
        self.txt.set(self.txt.get()[:-1])