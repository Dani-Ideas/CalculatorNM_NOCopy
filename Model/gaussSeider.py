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

# Ejemplos de uso

# Ejemplo 1
# Resolver el sistema:
# -46.658333*x1 - 8.680122*x2 - 1.650295*x3 = -10.308984
# 0.1*x1 + 1.286658*x2 + 0.524802*x3 = -1.929987
# 0.3*x1 - 0.2*x2 - 0.01*x3 = 0.0

A1 = np.array([
    [-46.658333, -8.680122, -1.650295],
    [0.1, 1.286658, 0.524802],
    [0.3, -0.2, -0.01]
])

b1 = np.array([-10.308984, -1.929987, 0.0])
x0_1 = np.zeros(len(b1))

# Llamada al método
print("Ejemplo 1:")
gaussSeidel(A1, b1, x0_1, 100, 0.001)

# Ejemplo 2
# Resolver el sistema:
# 4*x1 - x2 + x3 = 7
# -2*x1 + 6*x2 + x3 = 9
# x1 + x2 + 5*x3 = -6

A2 = np.array([
    [4, -1, 1],
    [-2, 6, 1],
    [1, 1, 5]
])

b2 = np.array([7, 9, -6])
x0_2 = np.zeros(len(b2))

# Llamada al método con 100 iteraciones máximas y tolerancia de 0.001
print("Ejemplo 2:")
gaussSeidel(A2, b2, x0_2, 100, 0.001)
