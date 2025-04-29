variable = False
E=2.1212
import Constantes#variables almacenadas en un modulo externo
#las variables las detecta de forma automatica ya sea int string bool ...
print(variable)
#las constantes
#se lo declara en mayusculas por normativa
print(E)
print(Constantes.Pi)#esto se usa cuando se usa variables en un modulo externo
#buena etica de programador se debe usar variables ya definidas y no variables vacias, por motivos de seguridad
#declaracion de variables dinamicas en una sola linea
a=b=c=8
#sirve para definir variables que se usan el mismo dato 
print(c)
print(b)
print(a)
#definir variables en una sola linea con diferentes datos
d,e,f=9,10,11
print(f)
print(e)
print(d)