#modulos en Python librerias
import miPrimerModulo
'''
def suma(a,b):
    resultado = a+b
    return resultado
def resta(a,b):
    resultado = a-b 
    return resultado
def multiplicacion(a,b):
    resultado = a*b
    return resultado
'''
'''
numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
suma=miPrimerModulo.suma(numero,numero2)
resta=miPrimerModulo.resta(numero,numero2)
multiplicacion=miPrimerModulo.multiplicacion(numero,numero2)
print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicacion es: ",multiplicacion)
'''
numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
suma=miPrimerModulo.suma(numero,numero2)
resta=miPrimerModulo.resta(numero,numero2)
multiplicacion=miPrimerModulo.multiplicacion(numero,numero2)
print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicacion es: ",multiplicacion)
import esPar

# Solicitar al usuario que ingrese un número
n = int(input('Ingrese un número: '))

# Usar la función imprimir del módulo esPar
esPar.imprimir(n)
