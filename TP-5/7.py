"""
7. Cree una función que reciba dos string como parámetro (nombre1 y nombre2), y retorne True si nombre1 tiene más letras que nombre2, o False en caso contrario. nom1=input("Ingrese Nombre 1 ")
"""

def compararLongitudesPalabras(palabra1, palabra2) :
    lenPalabra1 = len(palabra1)
    lenPalabra2 = len(palabra2)

    if lenPalabra1 > lenPalabra2 :
        res = True
    else :
        res = False

    return res

nombre1 = input("Ingrese el nombre 1: ")
nombre2 = input("Ingrese el nombre 2: ")

print(compararLongitudesPalabras(nombre1, nombre2))