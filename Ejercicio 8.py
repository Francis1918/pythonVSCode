#uso del bucle for y for each
exp = 2
frutas = ['Manzana','Banana','Cereza','Pera',"Naranja"]#un arreglo o array
contador= 0
#bucle for each que itera en el arreglo de la lista de frutas
#variable de control se la usara fruta
'''
for fruta in frutas:
    #incremento del contador con mas 1 posicion
    contador+=1
    #f es un request focus o enter en la impresion
    print(f'Fruta #{contador}:{fruta}')
    if contador == 6:
        contador=0
'''
'''
#lista de numeros
n= [1,2,3,4,5]
for num in n:
    pow = num**exp
    print(f'El numero {num} elevado a la {exp} es {pow}')
'''
#En el bucle for se lo usa en casos que se requiera que haga una iteracion
'''
numeros =[10,5,9,8,2,10,10]
suma = 0
#tamaño del arreglo
n=len(numeros)     
for numero in numeros:
    #suma acumuladora similar a acumular las frecuencias absolutas en Estadistica Descriptiva
    suma= suma + numero
promedio=suma/n
print('El promedio es:', promedio)
'''
#para escribir un bucle for similar al lenguaje C
#for(int i=0;i<=11;i++)
#su forma equivalente en Python es:
#la funcion range(i,j), es un intervalo que si yo decido inicializar en un valor punutual 
#lo inicializaria en como esta en la sintaxis
#y si quiero que inicializaria en cero se usaria la siguiente manera:
#range(12)
#tomando en cuenta que la funcion range es un intervalo semiabierto hacia la derecha ya 
#que no incluye el ultimo punto x<12
li=2
ls=12
for i in range(li,ls):
    print(i)
    #para reiniciar el contador a la posicion inicial
    if i==ls-1:
        i=li
print(i)
#esta es la sintaxis completa de la funcion range
'''
La función range() en Python tiene la siguiente sintaxis:
Con un argumento:
range(stop)
stop: Número entero que indica hasta dónde (exclusivo) genera la secuencia.
La secuencia comienza en 0 y termina antes de stop.
Con dos argumentos:
range(start, stop)
start: Número entero que indica el valor inicial (inclusive) de la secuencia.
stop: Número entero que indica el valor final (exclusivo) de la secuencia.
Con tres argumentos:
range(start, stop, step)
start: Valor inicial de la secuencia.
stop: Valor final, exclusivo.
step: Incremento o decremento entre cada valor de la secuencia. Por defecto es 1, pero puede ser negativo para generar secuencias decrecientes.
'''
'''
1. Recorrido Secuencial (De Inicio a Fin)
El método más directo es iterar sobre cada elemento de la lista:

python
numeros = [10, 5, 9, 8, 2, 10, 10]
for num in numeros:
    print(num)
> Descripción: > Este bucle recorre la lista desde el primer elemento hasta el último, en el orden original.

2. Recorrido Inverso
Puedes recorrer la lista en orden inverso de varias maneras:

a) Usando la función reversed()
python
for num in reversed(numeros):
    print(num)
> Descripción: > La función reversed() devuelve un iterador que recorre la lista en orden inverso sin necesidad de crear una copia adicional.

b) Usando Slicing ([::-1])
python
for num in numeros[::-1]:
    print(num)
> Descripción: > Esta técnica utiliza el slicing para crear una copia inversa de la lista y luego la recorre.

c) Usando índices con range() y un paso negativo
python
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])
> Descripción: > Aquí se recorre la lista usando índices, iniciando desde el último índice hasta el primero, decrementando de uno en uno.

3. Recorrido con Índices (Acceso Posicional)
Si necesitas trabajar con el índice de cada elemento, puedes usar la función range() o enumerate():

a) Con range()
python
for i in range(len(numeros)):
    print(f"Índice {i}: {numeros[i]}")
> Descripción: > Este método te permite obtener el índice y el elemento, en el orden natural de la lista.

b) Con enumerate()
python
for indice, num in enumerate(numeros):
    print(f"Índice {indice}: {num}")
> Descripción: > enumerate() es particularmente útil porque te proporciona directamente el índice y el valor, haciendo el código más legible.

4. Recorrido Seleccionando un Orden Personalizado
Si necesitas recorrer la lista en un orden específico o personalizado (por ejemplo, ordenarlos antes de recorrerlos), puedes usar la función sorted():

python
for num in sorted(numeros):
    print(num)
> Descripción: > Aquí se recorre la lista ordenada de menor a mayor. Puedes invertir el orden usando el parámetro reverse=True:

python
for num in sorted(numeros, reverse=True):
    print
'''