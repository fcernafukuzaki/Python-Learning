import numpy as np

## Operaciones con matrices
matriz = np.array([[1, -3 , 2], [5, 6, -1], [4, -1 ,3]])
vector = np.array([[-2], [5], [7]])
print('Matriz')
print(matriz)
print('Vector')
print(vector)

print('Matriz por Matriz')
multiplicacion_matriz_matriz = matriz * matriz
print(multiplicacion_matriz_matriz)

## Producto interno
print('')
print('P R O D U C T O   I N T E R N O')
print('Matriz por Vector')
producto_interno = matriz.dot(vector)
print(producto_interno)
print('Vector por Matriz')
vector = np.array([[-2, 5, 7]])
producto_interno = np.dot(vector, matriz)
print(producto_interno)

print('Matriz por Matriz')
multiplicacion_matriz_matriz = np.dot(matriz, matriz)
print(multiplicacion_matriz_matriz)

## Producto interno
print('')
print('T R A N S P O S I C I Ó N   D E   P R O D U C T O   I N T E R N O   D E   M A T R I C E S')
matriz_a = np.array([[2, 3], [5, 7], [11, 13]])
matriz_b = np.array([[1, 3], [2,1]])
print('Matriz A: {}'.format(matriz_a))
print('Matriz B: {}'.format(matriz_b))
print('Resultado 1:')
producto_matriz_matriz = np.dot(matriz_a, matriz_b)
#producto_matriz_matriz = matriz_a.dot(matriz_b).T
producto_matriz_matriz_t = producto_matriz_matriz.T
print(producto_matriz_matriz_t)
print('Resultado 2:')
producto_matriz_t_matriz_t = np.dot(matriz_b.T, matriz_a.T)
print(producto_matriz_t_matriz_t)
print('Validación de matrices:')
print(producto_matriz_matriz_t == producto_matriz_t_matriz_t)
