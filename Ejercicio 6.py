#uso de condicionales if else elif
#solo se ejecuta cuando el resultado es verdadero
x=10
edad = int(input('Por Favor Ingresa Tu Edad:'))
if edad <0:
    print('Valor ingresado No Valido, Por Favor Ingresa Nuevamente')
elif edad<12:
    print("Edad Registrada, Eres menor de Edad, Niño")
elif edad<18:
    print('Edad Regristrada, Eres menor de Edad, Adolecente')
elif edad<65:
    print('Edad Registradda, Eres Mayor de Edad, Adulto')
else:
    print("Edad Registrada, Eres mayor de Edad, Adulto Mayor")

'''
    print('X es mayor que 5')
elif x<15:
    print('X es menor que 15')
else:
    print('X es mayor igual que 15')

'''
