from tkinter import *
from math import sin, cos, tan, log, log10, sqrt, pow, sinh, cosh, tanh, degrees, radians, pi, e as euler_e
from Models.biseccition import MB_mostrar_tabla
from Models.NRaphsonMethod import NR_mostrar_tabla
import re

root = Tk()
root.title("CALCULATOR NUMERIC METHOTS")
root.geometry("600x625+50+40")  # Tamaño inicial, pero ahora será redimensionable
root.resizable(1, 1)  # Permite cambiar el tamaño de la ventana manualmente
chooseAlg=0 # es el numero del algoritmo que se decicio usar

F = Frame(root, bg="darkslateblue", bd=10, width=350, height=500)
F.pack(fill=BOTH, expand=True) 
 
# Create a Function to get Entry
def press(text):
    num = txt.get()
    if num == "Error":
        txt.set("Error")
    else:
        txt.set(num + text)
 
# Create a Function to Reset Entry 
def reset():
    txt.set("")
 
# Create a Function to Cancel Entry 
def cancel():
    txt.set(txt.get()[:-1])
 
# Create a Function to Calculation

def cal(functionSTR):
    try:
        expression = functionSTR
        # Usa eval con funciones matemáticas permitidas, incluyendo 'e' como 'euler_e'
        result = eval(expression, {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan, 
                                                           "log": log, "log10": log10, 
                                                           "sqrt": sqrt, "pow": pow, 
                                                           "sinh": sinh, "cosh": cosh, 
                                                           "tanh": tanh, "degrees": degrees, 
                                                           "radians": radians, "pi": pi, "e": euler_e})
        txt.set(result)
    except Exception as e:
        txt.set(f"Error: {e}")

def agregar_multiplicaciones_implicitas(expresion):
    # Lista de funciones matemáticas conocidas para la calculadora
    funciones = ["sin", "cos", "tan", "log", "log10", "sinh", "cosh", "tanh", "sqrt", "exp", "degrees", "radians"]
    
    # Compilamos las funciones en una sola expresión regular con agrupación para evitar conflictos
    funciones_regex = r'|'.join(funciones)

    # Patrón para encontrar multiplicaciones implícitas:
    # - Número o variable seguido de una función, variable, o apertura de paréntesis.
    patron = rf'(?<!\*\*)(\b\d+|\b[a-zA-Z])(?=({funciones_regex}|\bX\b|\b[a-zA-Z\(]))'
    
    # Agrega '*' donde detecta multiplicaciones implícitas y evita las funciones conocidas
    expresion_modificada = re.sub(patron, r'\1*', expresion)

    # Agrega '*' para casos específicos donde un número es seguido por 'X' o una apertura de paréntesis (ej. 12X -> 12*X)
    expresion_modificada = re.sub(r'(\d)(X|\()', r'\1*\2', expresion_modificada)
    
    # Agrega '*' para casos donde 'X' es seguido por una apertura de paréntesis (ej. X(12) -> X*(12))
    expresion_modificada = re.sub(r'X(?=\()', r'X*', expresion_modificada)
    
    # Agrega '*' para casos donde 'X' es seguido por un cierre de paréntesis (ej. (12)X -> (12)*X)
    expresion_modificada = re.sub(r'\)(?=X)', r')*', expresion_modificada)

    # Agrega '*' para casos donde 'e' es seguido por un número (ej. e8 -> e*8)
    expresion_modificada = re.sub(r'e(?=\d)', r'e*', expresion_modificada)

    # Agrega '*' para casos donde 'e' es seguido por un número (ej. 8e -> 8*e)
    expresion_modificada = re.sub(r'(\d)(e|\()', r'\1*\2', expresion_modificada)

    return expresion_modificada

def sustitucion(x, expresion):
    # Verifica si x es un número
    try:
        float_x = float(x)  # Intenta convertir x a float
    except ValueError:
        print("El valor de x debe ser un número.")
        return expresion  # Retorna la expresión sin cambios si x no es un número
    
    # Si x es un número, sustituye todas las 'X' en la expresión
    expresion_con_sustitucion = expresion.replace("X", str(float_x))
    
    return expresion_con_sustitucion

# Para la prueba
def analice():
    print(chooseAlg)
      #temporal
    if chooseAlg == 1:
        MB_mostrar_tabla()
    elif chooseAlg == 2:
        NR_mostrar_tabla()
    #el resto de  lo algortmos

    entrada = txt.get()
    resultadoX = agregar_multiplicaciones_implicitas(entrada)
    resultado = sustitucion(7, resultadoX)
    print("Expresión con multiplicaciones implícitas corregidas:", resultadoX)
    print("Expresión final tras sustitución:", resultado)
    cal(resultado)
  
# Función para cambiar la selección de botones
def chosseMN(boton_seleccionado):
    global chooseAlg 
    if boton_seleccionado == 1:#'bisec'
        chooseAlg=boton_seleccionado
        B81.config(bg="red", activebackground="IndianRed1")  # Botón Bisec se selecciona con rojo
        B82.config(bg="SlateGray2", activebackground="SlateGray2")  # Des-seleccionamos el botón del metodo num.
    elif boton_seleccionado == 2:#'newton'
        chooseAlg=boton_seleccionado
        B81.config(bg="SlateGray2", activebackground="SlateGray2")  
        B82.config(bg="red", activebackground="IndianRed1")
    elif boton_seleccionado == 3:#'Gauss E'
        chooseAlg=boton_seleccionado
        B81.config(bg="SlateGray2", activebackground="SlateGray2")  
        B82.config(bg="red", activebackground="IndianRed1")
    elif boton_seleccionado == 4:#'Lagrange'
        chooseAlg=boton_seleccionado
        B81.config(bg="SlateGray2", activebackground="SlateGray2")  
        B82.config(bg="red", activebackground="IndianRed1")  



""" ---------------View--------------- """
txt = StringVar()
Entry(F, textvariable=txt, font=("None 30 bold"), bg="yellow", bd=5).grid(columnspan=15, pady=10, ipadx=58, ipady=12)
 


B11 = Button(F, text="sin", command=lambda: press("sin("), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B11.grid(row=1, column=0)
B12 = Button(F, text="cos", command=lambda: press("cos("), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B12.grid(row=1, column=1)
B13 = Button(F, text="tan", command=lambda: press("tan("), font=("None 25 bold"),bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B13.grid(row=1, column=2)
B14 = Button(F, text="log", command=lambda: press("log("), font=("None 25 bold"),
             bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B14.grid(row=1, column=3)
B15 = Button(F, text="Clear", command=reset, font=("None 25 bold"),bd=4, width=5, bg="tomato", activebackground="red")
B15.grid(row=1, column=4)
 
 
B21 = Button(F, text="pow", command=lambda: press("**"), font=("None 25 bold"),bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B21.grid(row=2, column=0)
B22 = Button(F, text="sqrt", command=lambda: press("sqrt"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B22.grid(row=2, column=1)
B23 = Button(F, text="exp", command=lambda: press("exp"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B23.grid(row=2, column=2)
B24 = Button(F, text="log10", command=lambda: press("log10"), font=("None 25 bold"),bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B24.grid(row=2, column=3)
B25 = Button(F, text="Del", command=cancel, font=("None 25 bold"),bd=4, width=5, bg="orange", activebackground="goldenrod1")
B25.grid(row=2, column=4)
 
 
B31 = Button(F, text="sinh", command=lambda: press("sinh"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B31.grid(row=3, column=0)
B32 = Button(F, text="cosh", command=lambda: press("cosh"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B32.grid(row=3, column=1)
B33 = Button(F, text="tanh", command=lambda: press("tanh"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B33.grid(row=3, column=2)
B34 = Button(F, text="Deg", command=lambda: press("degrees"), font=("None 25 bold"),bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B34.grid(row=3, column=3)
B35 = Button(F, text="Rad", command=lambda: press("radians"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B35.grid(row=3, column=4)
 
B41 = Button(F, text="7", command=lambda: press("7"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B41.grid(row=4, column=0)
B42 = Button(F, text="8", command=lambda: press("8"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B42.grid(row=4, column=1)
B43 = Button(F, text="9", command=lambda: press("9"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B43.grid(row=4, column=2)
B44 = Button(F, text="*", command=lambda: press("*"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
B44.grid(row=4, column=3)
B45 = Button(F, text="/", command=lambda: press("/"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
B45.grid(row=4, column=4)
 
 
B51 = Button(F, text="4", command=lambda: press("4"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B51.grid(row=5, column=0)
B52 = Button(F, text="5", command=lambda: press("5"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B52.grid(row=5, column=1)
B53 = Button(F, text="6", command=lambda: press("6"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B53.grid(row=5, column=2)
B54 = Button(F, text="+", command=lambda: press("+"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
B54.grid(row=5, column=3)
B55 = Button(F, text="-", command=lambda: press("-"), font=("None 25 bold"),bd=4, width=5, bg="springgreen", activebackground="steelblue2")
B55.grid(row=5, column=4)
 
 
B61 = Button(F, text="1", command=lambda: press("1"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B61.grid(row=6, column=0)
B62 = Button(F, text="2", command=lambda: press("2"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B62.grid(row=6, column=1)
B63 = Button(F, text="3", command=lambda: press("3"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B63.grid(row=6, column=2)
B64 = Button(F, text="(", command=lambda: press("("), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue1")
B64.grid(row=6, column=3)
B65 = Button(F, text=")", command=lambda: press(")"), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue1")
B65.grid(row=6, column=4)
 
 
B71 = Button(F, text="π", command=lambda: press("pi"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B71.grid(row=7, column=0)
B72 = Button(F, text="0", command=lambda: press("0"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B72.grid(row=7, column=1)
B73 = Button(F, text=".", command=lambda: press("."), font=("None 25 bold"),bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B73.grid(row=7, column=2)
B74 = Button(F, text="e", command=lambda: press("e"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B74.grid(row=7, column=3)
#B75 = Button(F, text="Redy", command=cal, font=("None 25 bold"),bd=4, width=5, bg="lime", activebackground="cyan")
#B75.grid(row=7, column=4)

B75 = Button(F, text="Redy", command=analice, font=("None 25 bold"),bd=4, width=5, bg="lime", activebackground="cyan")
B75.grid(row=7, column=4)

B81 = Button(F, text="Bisec", font=("None 25 bold"), bd=4, width=5, bg="SlateGray1", activebackground="IndianRed1", command=lambda: chosseMN(1))
B81.grid(row=8, column=0)
B82 = Button(F, text="Newton", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: chosseMN(2))
B82.grid(row=8, column=1)
B83 = Button(F, text="Gauss.E", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: chosseMN(3))
B83.grid(row=8, column=2)
B84 = Button(F, text="Lagrange", font=("None 25 bold"), bd=4, width=5, bg="SlateGray2", activebackground="IndianRed1", command=lambda: chosseMN(4))
B84.grid(row=8, column=3)

chosseMN(1)

B85 = Button(F, text="X", command=lambda: press("X"),font=("None 25 bold"), bd=4, width=5, bg="gray", activebackground="lightgray")
B85.grid(row=8, column=4)
root.mainloop()