import numpy as np
import matplotlib.pyplot as plt
from FuncionesAuxiliares import GraficarVectores

v1 = np.array([2,5])
v2 = np.array([3,2])

# %run "..\\FuncionesAuxliares\graficarVectores.py"

GraficarVectores.graficarVectores([v1, v2], ['orange', 'blue'])
plt.xlim(-1, 8)
plt.ylim(-1, 8)

## Mostrar gráfico en pantalla
plt.show()
