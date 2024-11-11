import numpy as np

def gaussSeidel(A, b, x0, N, tol):
    """
    Método de Gauss-Seidel para resolver sistemas de ecuaciones lineales.

    Parámetros:
    A (numpy array): Matriz de coeficientes del sistema.
    b (numpy array): Vector de términos independientes.
    x0 (numpy array): Vector de inicialización.
    N (int): Número de iteraciones máximas.
    tol (float): Tolerancia para la convergencia.

    Retorna:
    x (numpy array): Solución aproximada del sistema.
    """
    max_iterations = N
    x = np.copy(x0)  # Inicializa x con el valor de x0
    xprev = np.zeros(len(b))  # Vector para almacenar el valor anterior de x

    for i in range(max_iterations):
        xprev = np.copy(x)  # Actualiza xprev con el valor actual de x
        for j in range(len(b)):
            summ = 0
            for k in range(len(b)):
                if k != j:
                    summ += A[j][k] * x[k]
            x[j] = (b[j] - summ) / A[j][j]  # Calcula el nuevo valor de x[j]

        # Calcula la norma para verificar la convergencia
        diff1norm = np.linalg.norm(x - xprev, ord=1)
        oldnorm = np.linalg.norm(xprev, ord=1)
        if oldnorm == 0:
            oldnorm = 1
        norm = diff1norm / oldnorm

        if norm < tol and i != 0:
            print("La solución converge en x:", x)
            return x

    print("La matriz no converge.")
    return None

""" 
Ejemplo de uso
Supongamos que queremos resolver el sistema de ecuaciones lineales:

-4.6658333e+01*x1 - 8.6801220e+00*x2 - 1.6502950e+00*x3 = -10.308984
0.1*x1 + 1.2866580e+00*x2 + 5.2480200e-01*x3 = -1.929987
0.3*x1 - 0.2*x2 - 1.0e-02*x3 = 0.0

Con la matriz A y el vector b definidos como:

A = np.array([
    [3.0, -0.1, -0.2],
    [0.1, 7.0, -0.3],
    [0.3, -0.2, -10.0]
])

b = np.array([7.85, -19.30, 71.40])

x0 = np.zeros(3)  # Vector de inicialización

gaussSeidel(A, b, x0, 3, 0.001)
A = np.array([
    [-4.6658333e+01, -8.6801220e+00, -1.6502950e+00],
    [0.1, 1.2866580e+00, 5.2480200e-01],
    [0.3, -0.2, -1.0e-02]
])

b = np.array([-10.308984, -1.929987, 0.0])
x0 = np.zeros(len(b))  # Vector de inicialización

# Llamada al método
gaussSeidel(A, b, x0, 100, 0.001)


# Definimos la matriz A y el vector b
B = np.array([
    [4, -1, 1],
    [-2, 6, 1],
    [1, 1, 5]
])

c = np.array([7, 9, -6])
x1 = np.zeros(len(b))  # Vector de inicialización

# Llamada al método con 100 iteraciones máximas y tolerancia de 0.001
gaussSeidel(B, c, x1, 100, 0.001)
"""