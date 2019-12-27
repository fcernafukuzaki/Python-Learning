import numpy as np
import matplotlib.pyplot as plt

# Sistema de ecuaciones:
#  y = 3x + 5
#  y = -x + 3
#  y = 2x + 1
#
# Despejamos las constantes:
#  -3x + y = 5
#    x + y = 3
#  -2x + y = 1
#

# Definir intervalor con los valores que tomará Y
# Los valores que puede tomar X son del -6 al 6.
x = np.arange(-6, 6)

y_1 = 3*x + 5
y_2 = -x + 3
y_3 = 2*x + 1

# Graficar sistema de ecuaciones:
plt.figure()
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_3)

plt.xlim(-8, 8)
plt.ylim(-8, 8)

plt.axvline( x=0, color='grey')
plt.axhline( y=0, color='grey')

## Mostrar gráfico en pantalla
plt.show()
#
# Conclusión:
#
# A partir del gráfico se puede observar que las tres líneas no se cruzan.
# El sistema de ecuaciones no tiene solución.
