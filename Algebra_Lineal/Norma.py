import numpy as np

print('Norma de un vector')

v1 = np.array([2, 7])
v2 = np.array([3, 5])

v1v2 = v1 + v2

norma_v1v2 = np.linalg.norm(v1v2)

norma_v1 = np.linalg.norm(v1)
norma_v2 = np.linalg.norm(v2)

print('La norma del vector 1 es {}'.format(norma_v1))
print('La norma del vector 2 es {}'.format(norma_v2))
print('La norma del vector es {}'.format(norma_v1v2))

# Desigualdad triangular
# norma(v1v2) <= norma (v1) + norma (v2)

print(norma_v1v2 <= norma_v1 + norma_v2)

print('T I P O S   D E   N O R M A S')
print('L0: Retorna la cantidad de elementos del vector que son distintos de cero.')
print('L1: Retorna la suma sobre i de los valores absolutos de los componentes del vector.')
#   abs(v_posicion1) + abs(v_posicion2) + abs(v_posicion3) + ...
print('L2: Distancia euclidiana. Cuánto mide un vector al origen.')
print('L2^2: L2 sin aplicar la raíz cuadrada.')
print('L infinito: El mayor valor de los valores absolutos dentro del vector.')
#   maximo abs(v_posicion_n)

vector = np.array([1, 2, 0, 5, 6, 0])
print(np.linalg.norm(vector, ord = 0))
# Resultado: 4. Cantidad de elementos diferentes de 0.

vector = np.array([1, -1, 1, -1, 1])
print(np.linalg.norm(vector, ord = 1))
# Resultado: 5. Suma de los valores absolutos de los elementos del vector.

vector = np.array([1, 1])
print(np.linalg.norm(vector)) # Por defecto retorna la norma 2.
print(np.linalg.norm(vector, ord = 2))
# Resultado: 1.41.

vector = np.array([1, 2, 3, 4, 5, 6])
print(np.linalg.norm(vector, ord = 2)**2)
# Resultado: 91.
print(vector.T.dot(vector))
# Resultado: 91.

vector = np.array([1, 2, 3, -100])
print(np.linalg.norm(vector, ord = np.inf))
# Resultado: 100.
