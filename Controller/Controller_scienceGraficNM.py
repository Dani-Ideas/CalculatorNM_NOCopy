from Model.Model_scienceGraficNM import agregar_multiplicaciones_implicitas
from Model.biseccition import mb_mostrar_tabla
from Model.NRaphsonMethod import nr_mostrar_tabla
from View.View_scienceGrficNM import CalculatorView
import tkinter as tk

class CalculatorController:
    def press(self, text):
        current = self.view.get_text()
        self.view.set_text(current + text)

    def reset(self):
        self.view.set_text("")

    def cancel(self):
        current = self.view.get_text()
        self.view.set_text(current[:-1])

    def calculate(self):
        entrada = self.view.get_text()
        valueX = [float(value) for value in self.view.get_valueX() if value]
        resultadoX = agregar_multiplicaciones_implicitas(entrada)
        #temporal
        if self.chooseAlg == 1:
            mb_mostrar_tabla(valueX,resultadoX)
        elif self.chooseAlg == 2:
            nr_mostrar_tabla(valueX,resultadoX)

        """ resultado = sustituir_variable(7, resultadoX)  # Sustituye 'X' por un valor, ej: 7
        final_result = calcular_expresion(resultado) 
        self.view.set_text(final_result)
        """
    
    def chosseMN(self,boton_seleccionado):
        if boton_seleccionado == 1:#'bisec'
            self.chooseAlg=boton_seleccionado
            self.view.B81.config(bg="red", activebackground="IndianRed1")  # Botón Bisec se selecciona con rojo
            self.view.B82.config(bg="SlateGray2", activebackground="SlateGray2")  # Des-seleccionamos el botón del metodo num.
            self.view.B83.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B84.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.hidden_frame.grid(row=0, column=1, padx=10, sticky="nsew")
            self.view.label1.config(text="X1")
            self.view.label2.config(text="X2")
        elif boton_seleccionado == 2:#'newton'
            self.chooseAlg=boton_seleccionado
            self.view.B81.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B83.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B84.config(bg="SlateGray2", activebackground="SlateGray2")  
            self.view.B82.config(bg="red", activebackground="IndianRed1")
            #self.view.entry2.delete(0, tk.END)
            #self.view.entry3.delete(0, tk.END)
            #self.view.hidden_frame.grid_forget() 
        elif boton_seleccionado == 3:#'Gauss E'
            self.chooseAlg=boton_seleccionado
            self.view.B81.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B82.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B84.config(bg="SlateGray2", activebackground="SlateGray2")  
            self.view.B83.config(bg="red", activebackground="IndianRed1")
        elif boton_seleccionado == 4:#'Lagrange'
            self.chooseAlg=boton_seleccionado
            self.view.B81.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B82.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B83.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B84.config(bg="red", activebackground="IndianRed1")  

    def __init__(self, root):
        self.chooseAlg=0
        self.view = CalculatorView(root, self)
        self.chosseMN(1)