#uso de tuplas es para almacenar datos de manera ordenada y no se pueden modificar
#uso de tuplas se usa para eqn math, bases etc, se le usa con una coma para ingresar mas
#datos en un tupla
'''
mi_tupla = (1,2,3)
mi_tupla2= ('Manzana','Banana','Cereza')
mi_tupla3= (1,'Hola',3.14)
tupla_vacia = ()
posicion=0
print(mi_tupla[posicion])
print(mi_tupla2[posicion])
print(mi_tupla3[posicion])
'''
'''
personas = (('Juan', '25'), ('Maria','16'), ('Carlos','20'))
for nombre, edad in personas:
    if edad>'18':
        print('Mayor de edad')
        print(nombre, edad)
    else:
        print('Menor de edad')
        print(nombre, edad)
  
'''
'''
numeros =(10,20,30,40,50,100,5000,100000 )#tupla de solo numeros
suma= sum(numeros)#suma de los numeros de la tupla
#metodo sum() suma los elementos de una tupla que lo conforma
print(suma)
'''
#tarea
palabras = ("Manzana",'Banana','Cereza')
palabra_buscar = input('Ingrese la palabra a buscar: ')
if palabra_buscar in palabras:
    print('La palabra esta en la tupla')
else:
    print('La palabra no esta en la tupla')