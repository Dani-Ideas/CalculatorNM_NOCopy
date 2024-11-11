from math import sin, cos, tan, log, log10, sqrt, pow, sinh, cosh, tanh, degrees, radians, pi, e as euler_e
import re

def calcular_expresion(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan, 
                                                           "log": log, "log10": log10, 
                                                           "sqrt": sqrt, "pow": pow, 
                                                           "sinh": sinh, "cosh": cosh, 
                                                           "tanh": tanh, "degrees": degrees, 
                                                           "radians": radians, "pi": pi, "e": euler_e})
        return result
    except Exception as e:
        return f"Error: {e}"

def agregar_multiplicaciones_implicitas(expresion):
    funciones = ["sin", "cos", "tan", "log", "log10", "sinh", "cosh", "tanh", "sqrt", "exp", "degrees", "radians"]
    funciones_regex = r'|'.join(funciones)
    patron = rf'(?<!\*\*)(\b\d+|\b[a-zA-Z])(?=({funciones_regex}|\bX\b|\b[a-zA-Z\(]))'
    
    expresion_modificada = re.sub(patron, r'\1*', expresion)
    expresion_modificada = re.sub(r'(\d)(X|\()', r'\1*\2', expresion_modificada)
    expresion_modificada = re.sub(r'X(?=\()', r'X*', expresion_modificada)
    expresion_modificada = re.sub(r'\)(?=X)', r')*', expresion_modificada)
    expresion_modificada = re.sub(r'e(?=\d)', r'e*', expresion_modificada)
    expresion_modificada = re.sub(r'(\d)(e|\()', r'\1*\2', expresion_modificada)

    return expresion_modificada

def sustituir_variable(x, expresion):
    try:
        float_x = float(x)
    except ValueError:
        return expresion
    return expresion.replace("X", str(float_x))
