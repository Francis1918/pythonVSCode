'''
#diccionarios se lo usa con la siguiente sintaxis
#Usa una clave principal y un valor asociado a esa clave
#La clave es unica y no se puede repetir
#Los valores pueden ser de cualquier tipo ya sea entero o flotante
#o incluso otro diccionario
persona={
    'Nombre':'Juan',
    "Edad":30,
    'Ciudad':'Madrid'
}
perfil=persona#Variable de control para acceder a los datos del diccionario persona
print(perfil['Nombre'])#Imprime el valor asociado a la clave Nombre
print(perfil['Edad'])#Imprime el valor asociado a la clave Edad
print(perfil['Ciudad'])#Imprime el valor asociado a la clave Ciudad
#usamos la clave que esta asociado al dato que queremos modificar
'''
'''
#declaracion de un diccionario anidado
personas={
    'persona1':{
       'Nombre':'Juan',
        "Edad":30,
        'Ciudad':'Madrid' 
    },
    'persona2':{
       'Nombre':'Maria',
        "Edad":28,
        'Ciudad':'Barcelona' 
    },
    'persona3':{
       'Nombre':'Carlos',
        "Edad":35,
        'Ciudad':'Valencia' 
    }
}
datos=personas['persona1']#variable de control para acceder a los datos del diccionario personas
print(datos)
datos2=personas['persona2']
print(datos2)
datos3=personas['persona3']
print(datos3)
print('---------------------------------')
print(datos['Nombre'])
print(datos2['Edad'])
print(datos3['Ciudad'])
print('---------------------------------')
#Es una iteracion perfecta sobre los objetos de este diccionario
#diccionario vacio para que el user lo vaya llenando
persona1={
    'Nombre':None,#None es un valor vacio
    "Edad":None,
    'Direccion':None,
    'Telefono':None
}
persona1['Nombre']=input('Ingrese su nombre: ')
persona1['Edad']=int(input('Ingrese su edad: ')) 
persona1['Direccion']=input('Ingrese su direccion: ')
persona1['Telefono']=input('Ingrese su telefono: ')
print('---------------------------------')
print(persona1["Nombre"],'tiene',persona1['Edad'],'años,','vive en',persona1['Direccion'],'y su telefono es',persona1['Telefono'])
print('---------------------------------')
print(persona1)
'''
datos_personales={
    'Nombre':None,
    'Edad':None,
    'Direccion':None,
    'Telefono':None
}
datos_personales['Nombre']=input('Ingrese su nombre: ')
datos_personales['Edad']=int(input('Ingrese su edad: '))
datos_personales['Direccion']=input('Ingrese su direccion: ')
datos_personales['Telefono']=int(input('Ingrese su telefono: '))
print('---------------------------------')
print(datos_personales['Nombre'],'tiene',datos_personales['Edad'],'años,','vive en',datos_personales['Direccion'],'y su telefono es',datos_personales['Telefono'])