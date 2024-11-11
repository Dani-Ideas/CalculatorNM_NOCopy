from View.viewDivSin import ViewDivSin
from Model.modelCalcDivSin import ModelCalcDivSin
import tkinter as tk

class ControllerDivSin:
    def __init__(self, root):
        self.model = ModelCalcDivSin()
        self.view = ViewDivSin(root, self)
        self.update_clock()

    def update_clock(self):
        current_time = self.model.get_current_time()
        current_date = self.model.get_current_date()
        self.view.update_clock_label(current_time, current_date)
        self.view.root.after(1000, self.update_clock)

    def validate_numeric_input(self, value_if_allowed):
        return value_if_allowed.isdigit() or value_if_allowed == ""

    def create_labels(self):
        try:
            num_labels = int(self.view.num_labels_var.get())  
        except ValueError:
            num_labels = 0

        self.view.update_labels(num_labels) 
    
    def save_values(self):
        values = [float(entry.get()) for entry in self.view.entries]
        roots, poly_pretty = self.model.calcular_division_sintetica(values)

        # Limpiamos los resultados anteriores
        for widget in self.view.result_frame.winfo_children():
            widget.destroy()

        # Mostrar el polinomio
        poly_label = tk.Label(self.view.result_frame, text=f"Polinomio: {poly_pretty}")
        poly_label.pack()

        # Mostrar las raíces
        roots_label = tk.Label(self.view.result_frame, text=f"Raíces: {roots}")
        roots_label.pack()