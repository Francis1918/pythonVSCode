def esPar(n):
    if n % 2 == 0:
        return True
    else:
        return False

def esImpar(n):
    if n % 2 != 0:
        return True
    else:
        return False

def imprimir(n):
    if esPar(n):
        print("El número es par")
    else:
        print("El número es impar")

