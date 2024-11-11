import tkinter as tk
from Controller.Controller_scienceGraficNM import CalculatorController
from Controller.controllerDivSin import ControllerDivSin


class ControllerPrincipal:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.bind_buttons()

    def bind_buttons(self):
        self.view.calculadora_button.config(command=self.launch_calculadora)
        self.view.otra_funcion_button.config(command=self.launch_divicion_sintetica)

    def launch_calculadora(self):
        root_calculadora = tk.Toplevel(self.view.root)  
        CalculatorController(root_calculadora)

    def launch_divicion_sintetica(self):
        root_calculadoraSin = tk.Toplevel(self.view.root)  
        root_calculadoraSin.title("Caluladora de divicion sintetica")
        ControllerDivSin(root_calculadoraSin)
          

