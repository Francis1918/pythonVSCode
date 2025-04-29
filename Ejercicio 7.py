#la sentencia match o switch case
#es la alternativa al if elif else
#sentencia match para numeros
#solo imprime la primera que es la verdadera en caso que haya mas de una 
# coincidencia
'''
numero = 2
match numero:
    case 1:
        print('Uno')
    case 2:
        print('Dos')
    case 3:
        print('Tres')
    case _:
        print('Numero desconocido')
''' 

#sentencia match para caracteres
'''
numero = 'c'
match numero:
    case 'a':
        print('Uno')
    case 'b':
        print('Dos')
    case 'c':
        print('Tres')
    case _:
        print('Numero desconocido')
'''
numero = int (input('Por Favor Ingrese un Numero entero:'))
'''
match numero:
    case 0:
        print('tu numero es un Cero (0)')
    case numero if numero % 2 ==0:
        print('Tu Numero Ingresado:(', numero,'), Es Par')
    case numero if numero % 2 !=0:
        print('Tu Numero Ingresado:(', numero,'), No es Par')
    case _:
        print('Valor no Valido, Por Favor Ingrese de Nuevo')
'''
match numero:
    case numero if numero<0:
        print('Tu numero ingresado:(',numero,'), Pertenece al Intervalo de los numeros negativos x<0')
    case numero if numero>=0 and numero<10:
        print('Tu numero ingresado:(',numero,'), Pertenece al Intervalo de los numeros 0<=x<10')
    case numero if numero>=10:
        print('Tu numero ingresado:(',numero,'), Pertenece al Intervalo de los numeros x>=10')
    case _:
        print('Por Favor Ingresa un Numero Valido')