from Models.Model_scienceGraficNM import calcular_expresion, agregar_multiplicaciones_implicitas, sustituir_variable
from Models.biseccition import mb_mostrar_tabla
from Models.NRaphsonMethod import nr_mostrar_tabla
from Views.View_scienceGrficNM import CalculatorView


class CalculatorController:
    def __init__(self, root):
        self.chooseAlg=0
        self.view = CalculatorView(root, self)

    def press(self, text):
        current = self.view.get_text()
        self.view.set_text(current + text)

    def reset(self):
        self.view.set_text("")

    def cancel(self):
        current = self.view.get_text()
        self.view.set_text(current[:-1])

    def calculate(self):
        print(self.chooseAlg)
        #temporal
        if self.chooseAlg == 1:
            mb_mostrar_tabla()
        elif self.chooseAlg == 2:
            nr_mostrar_tabla()
        #el resto de  lo algortmos

        entrada = self.view.get_text()
        resultadoX = agregar_multiplicaciones_implicitas(entrada)
        resultado = sustituir_variable(7, resultadoX)  # Sustituye 'X' por un valor, ej: 7
        final_result = calcular_expresion(resultado)
        self.view.set_text(final_result)
    
    def chosseMN(self,boton_seleccionado):
        if boton_seleccionado == 1:#'bisec'
            self.chooseAlg=boton_seleccionado
            self.view.B81.config(bg="red", activebackground="IndianRed1")  # Botón Bisec se selecciona con rojo
            self.view.B82.config(bg="SlateGray2", activebackground="SlateGray2")  # Des-seleccionamos el botón del metodo num.
            self.view.B83.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B84.config(bg="SlateGray2", activebackground="SlateGray2")
        elif boton_seleccionado == 2:#'newton'
            self.chooseAlg=boton_seleccionado
            self.view.B81.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B83.config(bg="SlateGray2", activebackground="SlateGray2")
            self.view.B84.config(bg="SlateGray2", activebackground="SlateGray2")  
            self.view.B82.config(bg="red", activebackground="IndianRed1")
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
