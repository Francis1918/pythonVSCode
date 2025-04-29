#Uso de funciones en Python
'''
def saludar(nombre):
    print('Hola!', nombre)
def imprimir():
    print('Hola! Mundo')
saludar('Juan')
imprimir()
'''
'''
def suma(a, b):
    resultado = a + b
    return resultado
numero = int(input('Ingrese un numero: '))
numero2 = int(input('Ingrese otro numero: '))
resultado = suma(numero, numero2)#uso una variable de control para llamar a la funcion con los parametros que los necesita
print('La suma es: ', resultado)
'''
'''
def esPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
numero = int(input('Ingrese un numero: '))
if esPar(numero)==True:
    print(f'{numero} es par')
else:
    print(f'{numero} es impar') 
'''
'''
def listaNumeros(lista):
    maximo = max(lista)#max() devuelve el valor maximo de una lista de numeros
    return maximo
numeros = [10,40,50,5,6]
valor=listaNumeros(numeros)
print('El valor maximo almacenado en la lista es:', valor)
'''

def calculadora(num1, num2, operacion):
    match operacion:
        case '+':
            resultado = num1 + num2
            return resultado
        case '-':
            resultado = num1 - num2
            return resultado
        case '*':
            resultado = num1 * num2
            return resultado
        case '/':
            if num2 != 0:
                resultado = num1 / num2
                return resultado
            else:
                return 'Error: División por cero'
        case _:
            return 'Error: Por favor ingrese una operación válida'

# Solicitar al usuario que ingrese dos números y la operación
num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
operacion = input('Ingrese la operación (+, -, *, /): ')

# Llamar a la función calculadora y mostrar el resultado
resultado = calculadora(num1, num2, operacion)
print('El resultado es:', resultado)