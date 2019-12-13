import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt

escalar = 4
print('Escalar {}'.format(escalar))

vector = np.array([1, 2, 3, 4])
print('Vector {}'.format(vector))

matriz = np.array([[1, 2, 3] , [4, 5, 6] , [7, 8, 9]])
print('Matriz {}'.format(matriz))

tensor = np.array([
            [[256, 256, 256]] ,
            [[0, 0, 0]] ,
            [[126, 126, 126]]
            ])
print('Tensor {}'.format(tensor))

plt.imshow(tensor, interpolation = 'nearest')
plt.show()
