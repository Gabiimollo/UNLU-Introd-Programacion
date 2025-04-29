"""
5. Cree una función que reciba un string como parámetro, y retorne el mismo string, pero con todas las letras convertidas a mayúsculas.
6. Modifique la función del ejercicio anterior para que retorne dos versiones del string recibido como parámetro: primero la versión en minúsculas, y luego la versión en mayúsculas. 
"""

def convertirMayuscula(palabra) :
    return palabra.upper()

def convertirMinusculas(palabra) :
    return palabra.lower()

palabra = input("Ingrese una palabra: ")
print(f" - Palabra en minisculas: {convertirMinusculas(palabra)} \n - Palabra en Mayuscula: {convertirMayuscula(palabra)}")