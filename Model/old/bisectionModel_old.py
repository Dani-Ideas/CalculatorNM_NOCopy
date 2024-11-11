from Model.CalculatorModel import CalculatorModel

class ModelBisection:
    def __init__(self, function, x1, x2, tolerance=1e-6, max_iterations=100):
        self.function = function
        self.x1 = x1
        self.x2 = x2
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.calculator = CalculatorModel()  # Instancia para evaluar la función
        self.tableResults = []  # Lista para almacenar los resultados de cada iteración
    
    def sign_criterion(self, a, b):
        return -1 if (float(a) * float(b)) < 0 else 1

    def midpoint(self, a, b):
        return (a + b) / 2
    
    def bisection_method(self):
        
        f_x1 = self.calculator.evaluate_expression(self.function, self.x1)
        f_x2 = self.calculator.evaluate_expression(self.function, self.x2)
        
        # Validar si los signos de f(x1) y f(x2) son opuestos
        if self.sign_criterion(f_x1, f_x2) > 0:
            return "Error: No hay un cambio de signo entre f(x1) y f(x2)\nEn un futuro apliar el rango de busqueda de una forma inteligente"
        else:
            for iteration in range(self.max_iterations):
                mid = self.midpoint(self.x1, self.x2)
                f_mid = self.calculator.evaluate_expression(self.function, mid)

                # Guardar los resultados en la tabla
                self.tableResults.append({
                    "iteration": iteration + 1,
                    "x1": self.x1,
                    "x2": self.x2,
                    "midpoint": mid,
                    "f(mid)": f_mid
                })

                # Si f(mid) es cercano a 0 dentro de la tolerancia, hemos encontrado la raíz
                if abs(float(f_mid)) < self.tolerance:
                    return mid

                # Decidir el nuevo intervalo [x1, x2]
                if self.sign_criterion(f_x1, f_mid) < 0:
                    self.x2 = mid  # La raíz está entre x1 y mid
                else:
                    self.x1 = mid  # La raíz está entre mid y x2
            
        return "Error: No se encontró la raíz dentro del máximo número de iteraciones"
