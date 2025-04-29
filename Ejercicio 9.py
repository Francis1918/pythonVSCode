#funcion while o sentencia while
#solo calculos secundarios de manera logica por ejemplo de pasos de resolucion matematica
'''
contador = 1 
while contador<=5:
    print(contador)
    contador = contador +1
    #reinicio el valor del contador
    if contador ==6:
        contador =1
        #sin el break se repite la funcion while
        break
print(contador)
'''
'''
contador = 10
while contador>=1:
    print(contador)
    contador = contador -1
    if contador ==0:
        print('Feliz Año Nuevo')
        contador=10
        break
print(contador)
'''
'''
suma=0
numero= int(input("Por Favor Ingrese un Numero Natural, o Un Numero negativo para salir: "))
while numero>=0:
    suma = suma + numero
    numero= int(input("Por Favor Ingrese un Numero Natural, o Un Numero negativo para salir: "))
    print('La suma de los numeros Ingresados es:',suma)
    if numero<0:
        print('Fin del Programa')
        suma =0
        break

'''
contador =1
numero=int(input('Por Favor Ingrese el numero limite del contador:'))
while contador<=numero:
    print(contador)
    contador=contador+1#si coloco esta linea antes del print, el contador no se mostrara su valor inicial
    if contador==numero:
        print('Conteo Completado')
        contador=1
        break
print('Contador Reestablecido al valor inicial:',contador)