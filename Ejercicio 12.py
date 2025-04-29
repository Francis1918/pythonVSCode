'''
# listas en Python
n = 2
numeros = [1, 2, 3, 4, 5]  # lista numerica
frutas = ['manzana', 'banana', 'cereza']  # lista con cadenas
mixto = [1, 'Hola', 3.14, False]  # mixta lista
print(frutas[n])
print(numeros[n])
#para modificar un elemento de la lista
numeros[n]= 9
print(numeros[n])
print(numeros)
#agregar un numero mas a los elementos de la lista
numeros.append(8)#como es un numero entero se le puede poner directo sin ''
print(numeros)#imprimo los valores que existen en la lista con datos quemados
#agregar caracteres a la lista
print(frutas)
frutas.append('Coco')
print(frutas)
#uso de la palabra reservada del para eliminar un elemento de la lista
del numeros[n]
print(numeros)
del frutas[0]
print(frutas)
#uso de la palabra reservada del para eliminar la lista completa
#del numeros
for fruta in frutas:
    print(fruta)#vemos lo que se almacena en la lista dato por dato
suma= sum(numeros)#sumamos los elementos de la lista
print(suma)
'''
colores=['Rojo','Verde','Azul']
for color in colores:
    print(color)
