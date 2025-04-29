nombre = 'Francis'
apellido = 'BRAVO'
frase = 'Hola, esta es una frase'
p=4 #posicion
#metodo para contar todos los caracteres en una cadena
longitud = len(frase)#len() es un metodo que cuenta los caracteres de una cadena
print(longitud)
print(apellido[p])#extrae el caracter que necesitamos y las posiciones se usa del cero en adelante
#para el caso que haya cadenas de textos largas y buscar palabras se usa split()
palabras = frase.split()
print(palabras)
mayusculas = apellido.upper()#convierte a mayusculas la palabra
print(mayusculas)
mayusculas = frase.upper()#convierte a mayusculas la palabra
print(mayusculas)
texto = apellido.lower()#convierte a minusculas la palabra
print(texto)
mensaje = 'Hola, Mundo'
print(mensaje)
cambio= mensaje.replace('Hola','Marco')#reemplaza la palabra Hola por Marco
print(cambio)
#para separar una cadena por caracteres
for x in apellido:
    print(x)