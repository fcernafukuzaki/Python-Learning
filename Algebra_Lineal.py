import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt

print('   A L G E B R A   L I N E A L   ')

escalar = 4.79
print('Escalar {}'.format(escalar))

vector = np.array([1, 2, 3, 4])
print('Vector {}'.format(vector))

matriz = np.array([[1, 2, 3, 4] , [4, 5, 6, 7] , [7, 8, 9, 10] , [10, 11, 22, 23]])
print('Matriz {}'.format(matriz))

tensor = np.array([
            [[1, 2, 3] , [4, 5, 6] , [7, 8, 9]] ,
            [[11, 12, 13] , [14, 15, 16] , [17, 18, 19]] ,
            [[21, 22, 23] , [24, 25, 26] , [27, 28, 29]] ,
            [[31, 32, 33] , [34, 35, 36] , [37, 38, 39]]
            ])
print('Tensor {}'.format(tensor))

## Mostrar gráfico con valores del tensor
# plt.imshow(tensor, interpolation = 'nearest')
# plt.show()

## Dimensiones
print('D I M E N S I O N E S')
print('\tDimesiones del vector {}'.format(vector.shape))
print('\tDimesiones de la matriz {}'.format(matriz.shape))
print('\tDimesiones del tensor {}'.format(tensor.shape))

## Cantidad de elementos
print('C A N T I D A D   D E   E L E M E N T O S')
print('\tCantidad de elementos del vector {}'.format(vector.size))
print('\tCantidad de elementos de la matriz {}'.format(matriz.size))
print('\tCantidad de elementos del tensor {}'.format(tensor.size))

## Transpuesta
print('T R A N S P U E S T A')
vector_t = vector.T
matriz_t = matriz.T
tensor_t = tensor.T
print('\tTanspuesta del vector {}'.format(vector_t))
print('\tTanspuesta de la matriz {}'.format(matriz_t))
print('\tTanspuesta del tensor {}'.format(tensor_t))

## Suma de matrices. Se realiza cuando las matrices tienen las mismas dimensiones.
print('S U M A   D E   M A T R I C E S')
matriz1 = np.array([[1, 2, 3] , [4, 5, 6] , [7, 8, 9]])
matriz2 = np.array([[31, 32, 33] , [34, 35, 36] , [37, 38, 39]])
suma_matrices = matriz1 + matriz2
print('\tSuma de matriz y matriz\n\t{}'.format(suma_matrices))
suma_matriz_escalar = matriz1 + escalar
print('\tSuma de matriz y escalar\n\t{}'.format(suma_matriz_escalar))
suma_matriz_vector = matriz + vector
print('\tSuma de matriz y vector\n\t{}'.format(suma_matriz_vector))
suma_matriz_vector = matriz + vector_t
print('\tTanspuesta del vector {}'.format(vector_t))
print('\tSuma de matriz y vector transpuesta\n\t{}'.format(suma_matriz_vector))
suma_vector_vector = vector + vector_t
print('\tSuma del vector y transpuesta de vector {}'.format(suma_vector_vector))

## Broadcast: extender un elemento de menor dimensión hasta completar las
##              dimensiones de un alemento de mayor dimensión.
print('B R O A D C A S T')
broadcast_vector = np.array([[1, 2, 3, 4, 5]])
broadcast_matriz = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
broadcast_matriz_vector = broadcast_matriz + broadcast_vector.T
print('\tSuma de matriz y vector {}'.format(broadcast_matriz_vector))

## multiplicación de matrices
matriz = np.array([[1, -3 , 2], [5, 6, -1], [4, -1 ,3]])
# vector = np.array([[-2, 5, 7]])
vector = np.array([[-2], [5], [7]])
multiplicacion = matriz * vector
print(matriz)
print(vector)
print('Multiplicacion')
print(multiplicacion)

## Producto interno
print('Producto interno de Matriz por Vector')
producto_interno = matriz.dot(vector)
print(producto_interno)
print('Producto interno de Vector por Matriz')
vector = np.array([[-2, 5, 7]])
producto_interno = np.dot(vector, matriz)
print(producto_interno)
