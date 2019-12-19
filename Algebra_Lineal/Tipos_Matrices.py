import numpy as np

print('M A T R I Z   I D E N T I D A D')
## Matriz con el valor 1 en la diagonal de dimensión 5x5
identidad = np.eye(5)
print(identidad)

print('')
print('P R O D U C T O   I N T E R N O   D E   M A T R I Z   I D E N T I D A D   C O N   V E C T O R')
## Retorna el mismo valor del vector
vector = np.array([[2], [3], [5], [7], [11]])
print(identidad.dot(vector))

print('')
print('O B T E N E R   I N V E R S A   D E   U N A   M A T R I Z')
A = np.array([[1, 0 , 1], [0, 1, 1], [-1, 1, 1]])
print(A)

inversa_A = np.linalg.inv(A)
print(inversa_A)
print('Resultado matriz identidad:')
print(A.dot(inversa_A))

print('')
print('M A T R I Z   S I N G U L A R')
## Es cuando no existe una inversa de una matriz
A = np.array([[1, 1], [1, 1]])
## Esta matriz no tiene inversa
#print(np.linalg.inv(A))

## Ax = B => x = B(A^-1)
