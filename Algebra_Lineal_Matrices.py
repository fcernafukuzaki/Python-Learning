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
