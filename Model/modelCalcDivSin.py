import time
import numpy as np
import sympy as sp

class ModelCalcDivSin:
    def __init__(self):
        self.resultados = []

    def calcular_division_sintetica(self, coeficientes):
        coeficientes= [int(x) for x in coeficientes]
        # Inicializamos las variables
        roots = []
        n = len(coeficientes) - 1

        # Convertimos los coeficientes en un polinomio de sympy
        x = sp.symbols('x')
        poly = sum(c * x**i for i, c in enumerate(reversed(coeficientes)))

        # Empezamos con el proceso de Ruffini
        while n > 1:
            # Intentamos encontrar una raíz entera
            for i in range(-100, 101):
                trial = np.polyval(coeficientes, i)
                if trial == 0:
                    roots.append(i)
                    # División Sintética
                    new_coeficientes = []
                    new_coeficientes.append(coeficientes[0])
                    for j in range(1, len(coeficientes) - 1):
                        new_coeficientes.append(new_coeficientes[-1] * i + coeficientes[j])
                    coeficientes = new_coeficientes
                    n -= 1
                    break
            else:
                break
              
        # Si no hemos encontrado todas las raíces, resolvemos la ecuación restante
        if n > 1:
            remaining_poly = np.poly1d(coeficientes)
            complex_roots = np.roots(remaining_poly)
            roots.extend(complex_roots)

        return roots, sp.pretty(poly)

    def obtener_resultados(self):
        return self.resultados
    
    def get_current_time(self):
        return time.strftime("%H:%M:%S")

    def get_current_date(self):
        return time.strftime("%d:%m:%Y")
