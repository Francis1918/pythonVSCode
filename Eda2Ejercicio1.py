cadena = input('ingrese una palabra')

# Eliminar espacios y convertir a minúsculas para una comparación más precisa
cadena_limpia = ''.join(cadena.split()).lower()

# Verificar si la cadena es un palíndromo
if cadena_limpia == cadena_limpia[::-1]:
    print(f"La cadena '{cadena}' es un palíndromo.")
else:
    print(f"La cadena '{cadena}' no es un palíndromo.")