import math

def modulo(vector):
    resultado = 0
    long_vector = len(vector)

    for index in range(long_vector):
        resultado += pow(vector[index], 2)

    return math.sqrt(resultado)

def producto_escalar(vector1, vector2):
    resultado = 0
    long_vector1 = len(vector1)
    long_vector2 = len(vector2)

    if long_vector1 == long_vector2:
        for index in range(long_vector1):
            resultado += vector1[index] * vector2[index]
        return resultado
    else:
        print('Ambos vectores deben tener misma longitud.')

def producto_vectorial(vector1, vector2):
    resultado = list()
    resultado_index = 0
    long_vector1 = len(vector1)
    long_vector2 = len(vector2)

    # Valores iniciales
    posicion2 = long_vector2 - 1
    posicion1 = posicion2 - 1
    posicion1_neg = long_vector1 - 1
    posicion2_neg = posicion1_neg - 1

    if long_vector1 == long_vector2:
        for index in range(long_vector1):

            resultado_index = vector1[posicion1] * vector2[posicion2] - vector1[posicion1_neg] * vector2[posicion2_neg]
            resultado.append(resultado_index)

            # Asignar siguiente posicion
            posicion1_aux = posicion1
            posicion1 = posicion2
            posicion2 = posicion1_aux - 1
            posicion1_neg_aux = posicion1_neg
            posicion1_neg = posicion2_neg - 1
            posicion2_neg = posicion1_neg_aux

        return resultado
    else:
        print('Ambos vectores deben tener misma longitud.')

if __name__ == '__main__':
    vector1 = [1,1,2]
    vector2 = [0,2,1]

    resultado = modulo(vector1)
    print('El modulo del vector es {}'.format(resultado))

    resultado = modulo(vector2)
    print('El modulo del vector es {}'.format(resultado))

    resultado = producto_escalar(vector1, vector2)
    if type(resultado) == int:
        print('El producto escalar es {}'.format(resultado))

    resultado = producto_vectorial(vector1, vector2)
    if type(resultado) == list:
        print('El producto vectorial es {}'.format(resultado))
