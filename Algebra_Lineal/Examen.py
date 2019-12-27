import numpy as np

## Sistema de ecuaciones
# y_1 = 7*x + 2
# y_2 = 3*x + 5
## Se despeja las constantes del sistema de ecuaciones y se convierte en matriz
## - 7 * x + 1 * y = 2
## - 3 * x + 1 * y = 5
A = np.array([[-7, 1], [-3, 5]])
B = np.array([[2], [5]])
print('Solución del sistema de ecuaciones:')
print('Matriz A: {}'.format(A))
print('Matriz B: {}'.format(B))
inversa_A = np.linalg.inv(A)
print('Solución del sistema de ecuaciones utilizando Inversa de la Matriz:')
print(inversa_A.dot(B))
# Resultado: x = 3/4 ; y = 7 + 1/4


# Las matrices singulares tienen inversa: NO
# Una matriz cuadrada se dice singular cuando no es invertible.


v1 = np.array([1/2, 1/2, 1/2, 1/2])
norma_v1 = np.linalg.norm(v1)
print('La norma del vector 1 es {}'.format(norma_v1))
# Resultado: 1


v1 = np.array([-50, -25, 0, 25, 100, -300])
norma_v1 = np.linalg.norm(v1, ord = 0)
print('La norma 0 del vector 1 es {}'.format(norma_v1))
# Resultado: 5


# ¿Producto interno es conmutativo?
# Si tengo A y B matrices, tal que es posible calcular el producto interno,
# hacer A.dot(B) siempre es lo mismo que hacer B.dot(A)
# No, solamente en casos particulares podria ser lo mismo.


A = np.array([[1, 2, 3], [3, 4, 5]])
B = np.array([[1, 2], [3, 4], [3, 4]])
print(A)
print(B)
print(A.dot(B))
print(B.dot(A))
# Resultado: En este caso siempre puedo calcular el producto interno, aunque da
# distinto resultado hacer A.dot(B) y B.dot(A)


# Producto interno
C = np. array([[1], [2]])
print(C.shape) # 2,1
print(B.dot(C))
# Resultado: Vector de 3,1 . 3 filas ; 1 columna.


# Calcular la dimensión de un tensor.
#   tensor.shape


# Transponer la matriz
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('Transpuesta de la matriz {}'.format(A.T))
# Resultado:
# [[ 1  5  9]
# [ 2  6 10]
# [ 3  7 11]
# [ 4  8 12]]


# Sistema de ecuaciones con 4 ecuaciones y 4 incognitas se puede representar:
# Resultado:
#   1 matriz A de 4x4
#   1 vector x de dimecion 4
#   1 vector b de dimecion 4


# Sistema de ecuaciones lineales en R2 tiene infinitas soluciones cuando:
# Resultado: Más variables que ecuaciones.
#   Todas las ecuaciones lineales que forman parte del sistema están sobre la
#   misma recta y por lo tanto todos los puntos de la recta son solución.


# Dimensión del escalar 3.1
escalar = 3.1
#print(escalar.shape)
# Resultado:
#   AttributeError: 'float' object has no attribute 'shape'


# Ángulo que forman los vectores:
v1 = np.array([0, 1])
v2 = np.array([1, 0])
norma_v1 = np.linalg.norm(v1)
norma_v2 = np.linalg.norm(v2)
print('Ángulo: {}'.format(norma_v1 * norma_v2 * np.cos(np.deg2rad(45))))
print('Ángulo: {}'.format(v1.T.dot(v2)))
print('Ángulo: {}'.format(v1.dot(v2.T))) # Si el ángulo es 0, entonces forman 90°
#Resultado: 90 grados


# Matriz simétrica: A == A.T


# Vectores ortogonales.
# v = 7, -7, 3
# u = 1, 1, 0
# w = 0, 0, 1
# Resultado: No, porque no todas las combinaciones entre los vectores dan 0 al
# calcular el producto interno.


# Si estoy en un espacio de dimensión 3 y tengo una matriz, ¿Cuántas filas/columnas
# ortogonales puedo tener como máximo.
# Resultado:
# 3 vectores ortogonales (filas o columnas), porque cuando quiera tener un vector
#  más ortonormal a todos los que ya tengo no será posible lograrlo con escalar
#  cantidad de dimensiones.


# Determinante de una Matriz
M = np.array([[1, 0, 0, 0, 0], [0, 2, 0, 0, 0], [0, 0, 3, 0, 0], [0, 0, 0, 4, 0], [0, 0, 0, 0, 5]])
print(np.linalg.det(M))
# Resultado: 120


# Tansponer una matriz
matriz1 = np.array([[1, 2, 3] , [4, 5, 6] , [7, 8, 9]])
print(matriz1.dot(matriz1))
print(matriz1.dot(matriz1).T)
# Resultado:
print(matriz1.T.dot(matriz1.T))


# Sumar la matriz con un escalar da lo mismo que hacer:
# (matriz + escalar)
# (matriz + vector)
