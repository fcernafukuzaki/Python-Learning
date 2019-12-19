import numpy as np
import matplotlib.pyplot as plt

## Graficar intervalo
x = np.arange(-5, 5)

## Sistema de ecuaciones
y_1 = 3*x + 5
y_2 = 2*x + 3

## Graficar el sistema de ecuaciones
plt.figure()

plt.plot(x, y_1)
plt.plot(x, y_2)

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')

## Mostrar gráfico en pantalla
#plt.show()

## Solución con producto interno
print('Solucion de sistema de ecuaciones con producto interno')
## Se despeja las constantes del sistema de ecuaciones y se convierte en matriz
## -3*x + 1*y = 5
## -2*x + 1*y = 3
##
## Producto Interno: [ -3  1 ] [ x ] = [ 5 ]
##                   [ -2  1 ] [ y ]   [ 3 ]
##
A = np.array([[-3, 1], [-2, 1]])
B = np.array([[5], [3]])
solucion_1 = np.array([[-2], [-1]])
print('Solución del sistema de ecuaciones:')
print(solucion_1)
print('Validación de la solución del sistema de ecuaciones:')
print(B == A.dot(solucion_1))
