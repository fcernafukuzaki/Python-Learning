def factorial(number):
  if number < 0:
    print('Debe ingresar un número mayor a 0.')
  elif number == 0:
    return 1
  else:
    return number * factorial(number - 1)

if __name__ == '__main__':
    result = factorial(int(input('Ingrese un número:')))
    if type(result) == int:
        print('El resultado es: ' + str(result))
