import tkinter as tk

class CalculatorView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("CALCULATOR NUMERIC METHODS")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{int(screen_width*.9)}x{screen_height}")
        self.root.resizable(1, 1)
        
        self.txt = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.F = tk.Frame(self.root, bg="#4A5BEB", bd=10, width=350, height=500)
        self.F.pack(fill=tk.BOTH, expand=True)

        tk.Entry(self.F, textvariable=self.txt, font=("None 30 bold"), bg="yellow", bd=5).grid(columnspan=15, pady=10, ipadx=58, ipady=12)
        self.create_buttons(self.F)

    def create_buttons(self, frame):
        self.B11 = tk.Button(self.F, text="sin", command=lambda: self.controller.press("sin("), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B11.grid(row=1, column=0)
        self.B12 = tk.Button(self.F, text="cos", command=lambda: self.controller.press("cos("), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B12.grid(row=1, column=1)
        self.B13 = tk.Button(self.F, text="tan", command=lambda: self.controller.press("tan("), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B13.grid(row=1, column=2)
        self.B14 = tk.Button(self.F, text="log", command=lambda: self.controller.press("log("), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B14.grid(row=1, column=3)
        self.B15 = tk.Button(self.F, text="Clear", command=self.controller.reset, font=("None 25 bold"),bd=4, width=5, bg="tomato", activebackground="red")
        self.B15.grid(row=1, column=4)

        self.B21 = tk.Button(self.F, text="pow", command=lambda: self.controller.press("**"), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B21.grid(row=2, column=0)
        self.B22 = tk.Button(self.F, text="sqrt", command=lambda: self.controller.press("sqrt"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B22.grid(row=2, column=1)
        self.B23 = tk.Button(self.F, text="exp", command=lambda: self.controller.press("exp"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B23.grid(row=2, column=2)
        self.B24 = tk.Button(self.F, text="log10", command=lambda: self.controller.press("log10"), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B24.grid(row=2, column=3)
        self.B25 = tk.Button(self.F, text="Del", command=self.cancel, font=("None 25 bold"),bd=4, width=5, bg="#57596B", activebackground="goldenrod1")
        self.B25.grid(row=2, column=4)

        self.B31 = tk.Button(self.F, text="sinh", command=lambda: self.controller.press("sinh"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B31.grid(row=3, column=0)
        self.B32 = tk.Button(self.F, text="cosh", command=lambda: self.controller.press("cosh"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B32.grid(row=3, column=1)
        self.B33 = tk.Button(self.F, text="tanh", command=lambda: self.controller.press("tanh"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B33.grid(row=3, column=2)
        self.B34 = tk.Button(self.F, text="Deg", command=lambda: self.controller.press("degrees"), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B34.grid(row=3, column=3)
        self.B35 = tk.Button(self.F, text="Rad", command=lambda: self.controller.press("radians"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B35.grid(row=3, column=4)

        self.B41 = tk.Button(self.F, text="7", command=lambda: self.controller.press("7"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B41.grid(row=4, column=0)
        self.B42 = tk.Button(self.F, text="8", command=lambda: self.controller.press("8"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B42.grid(row=4, column=1)
        self.B43 = tk.Button(self.F, text="9", command=lambda: self.controller.press("9"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B43.grid(row=4, column=2)
        self.B44 = tk.Button(self.F, text="*", command=lambda: self.controller.press("*"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
        self.B44.grid(row=4, column=3)
        self.B45 = tk.Button(self.F, text="/", command=lambda: self.controller.press("/"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
        self.B45.grid(row=4, column=4)

        self.B51 = tk.Button(self.F, text="4", command=lambda: self.controller.press("4"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B51.grid(row=5, column=0)
        self.B52 = tk.Button(self.F, text="5", command=lambda: self.controller.press("5"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B52.grid(row=5, column=1)
        self.B53 = tk.Button(self.F, text="6", command=lambda: self.controller.press("6"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B53.grid(row=5, column=2)
        self.B54 = tk.Button(self.F, text="+", command=lambda: self.controller.press("+"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
        self.B54.grid(row=5, column=3)
        self.B55 = tk.Button(self.F, text="-", command=lambda: self.controller.press("-"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
        self.B55.grid(row=5, column=4)

        self.B61 = tk.Button(self.F, text="1", command=lambda: self.controller.press("1"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B61.grid(row=6, column=0)
        self.B62 = tk.Button(self.F, text="2", command=lambda: self.controller.press("2"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B62.grid(row=6, column=1)
        self.B63 = tk.Button(self.F, text="3", command=lambda: self.controller.press("3"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B63.grid(row=6, column=2)
        self.B64 = tk.Button(self.F, text="(", command=lambda: self.controller.press("("), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue1")
        self.B64.grid(row=6, column=3)
        self.B65 = tk.Button(self.F, text=")", command=lambda: self.controller.press(")"), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue1")
        self.B65.grid(row=6, column=4)

        self.B71 = tk.Button(self.F, text="π", command=lambda: self.controller.press("pi"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B71.grid(row=7, column=0)
        self.B72 = tk.Button(self.F, text="0", command=lambda: self.controller.press("0"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
        self.B72.grid(row=7, column=1)
        self.B73 = tk.Button(self.F, text=".", command=lambda: self.controller.press("."), font=("None 25 bold"),bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B73.grid(row=7, column=2)
        self.B74 = tk.Button(self.F, text="e", command=lambda: self.controller.press("e"), font=("None 25 bold"), bd=4, width=5, bg="#FAF9F6", activebackground="steelblue1")
        self.B74.grid(row=7, column=3)
        #B75 = tk.Button(self.F, text="Redy", command=cal, font=("None 25 bold"),bd=4, width=5, bg="lime", activebackground="cyan")
        #B75.grid(row=7, column=4)

        self.B75 = tk.Button(self.F, text="Redy", command=self.controller.calculate, font=("None 25 bold"),bd=4, width=5, bg="lime", activebackground="cyan")
        self.B75.grid(row=7, column=4)

        self.B81 = tk.Button(self.F, text="Bisec", font=("None 25 bold"), bd=4, width=5, bg="SlateGray1", activebackground="IndianRed1", command=lambda: self.controller.chosseMN(1))
        self.B81.grid(row=8, column=0)
        self.B82 = tk.Button(self.F, text="Newton", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: self.controller.chosseMN(2))
        self.B82.grid(row=8, column=1)
        self.B83 = tk.Button(self.F, text="Gauss.E", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: self.controller.chosseMN(3))
        self.B83.grid(row=8, column=2)
        self.B84 = tk.Button(self.F, text="Lagrange", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: self.controller.chosseMN(4))
        self.B84.grid(row=8, column=3)

        self.B85 = tk.Button(self.F, text="X", command=lambda: self.controller.press("X"),font=("None 25 bold"), bd=4, width=5, bg="gray", activebackground="lightgray")
        self.B85.grid(row=8, column=4)

    def set_text(self, text):
        self.txt.set(text)

    def get_text(self):
        return self.txt.get()
    def cancel(self):
        self.txt.set(self.txt.get()[:-1])